# Generated by Django 4.0.6 on 2022-07-18 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='index',
            field=models.PositiveSmallIntegerField(verbose_name='Порядковый номер'),
        ),
    ]