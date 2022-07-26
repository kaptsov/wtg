import os
from hashlib import md5

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


def upload_pics(location_data, location):
    for position, img_url in enumerate(location_data['imgs']):

        response = requests.get(img_url)
        response.raise_for_status()

        cf = ContentFile(response.content, name=md5(response.content).hexdigest())
        Image.objects.create(place_id=location.id, img_file=cf, index=position)


class Command(BaseCommand):
    """
    command: python manage.py load_place <link_to_json_file>
    Команда для заполнения данными локации на карте.
    Принимает аргументом ссылку на json-файл с описанием локации или файл со списком таких ссылок.
    Если объекта нет в базе данных, он будет создан.
    Если объект существует, скрипт обновляет поля из данных по ссылке (кроме картинок и названия).
    Если файл содержит данные в неверном формате, ссылка игнорируется.
    """
    help = 'Load location info from a link to json file or from file with list of links'

    def add_arguments(self, parser):
        parser.add_argument('source', type=str)

    def fill_data_from_link(self, link):
        response = requests.get(link.strip())
        response.raise_for_status()
        location_data = response.json()

        if 'error' in location_data:
            raise requests.exceptions.HTTPError(location_data['error'])

        location, created = Place.objects.get_or_create(
            title=location_data['title'],
            defaults={
                'lng': location_data['coordinates']['lng'],
                'lat': location_data['coordinates']['lat'],
                'description_long': location_data['description_long'],
                'description_short': location_data['description_short'],
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Location {location.title} already exists, defaults updated.'))
            return

        upload_pics(location_data, location)

        self.stdout.write(self.style.SUCCESS(f'Successfully read file {link}'
                                             f'Created Location object: {location.title} \n'))

    def handle(self, *args, **kwargs):
        source = kwargs['source']
        if os.path.isfile(source):
            with open(source, 'r', encoding='utf-8') as file:
                list_of_links = file.readlines()
            for link in list_of_links:
                self.fill_data_from_link(link)

        else:
            self.fill_data_from_link(source)
