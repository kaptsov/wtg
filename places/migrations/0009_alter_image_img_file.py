# Generated by Django 4.0.6 on 2022-07-24 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_file',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
