# Generated by Django 4.0.6 on 2022-07-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_file',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='Положение по широте'),
        ),
    ]