# Generated by Django 4.0.6 on 2022-07-23 17:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_options_alter_image_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]
