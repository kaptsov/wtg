from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):

    title = models.TextField(max_length=200,
                             help_text='Не более 200 символов',
                             verbose_name='Название',
                             blank=True,
                             unique=True
                             )
    description_short = models.TextField(verbose_name='Короткое описание',
                                         blank=True
                                         )
    description_long = HTMLField(verbose_name='Полное описание',
                                 blank=True
                                 )
    lat = models.FloatField(verbose_name='Положение по широте')
    lng = models.FloatField(verbose_name='Положение по долготе')

    def __str__(self):
        return self.title


class Image(models.Model):

    place = models.ForeignKey(Place,
                              on_delete=models.CASCADE,
                              related_name='images',
                              verbose_name='Место')
    index = models.PositiveIntegerField(verbose_name='Порядковый номер',
                                        default=0,
                                        )
    img_file = models.ImageField(verbose_name='Изображение')

    class Meta:
        ordering = ['index']

    def __str__(self):
        return f'{self.index}-{self.place}'
