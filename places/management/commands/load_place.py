import os
from io import BytesIO
from urllib.parse import urlsplit

import requests
from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError, CommandParser

from places.models import Place


class Command(BaseCommand):
    help = 'Loads and parse JSON data of a new place by URL and adds it to DB'

    def add_arguments(self, parser: CommandParser):
        parser.add_argument('url')


    def fill_data_from_link(self):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_data = response.json()
        title = place_data.get('title')
        if not title:
            raise CommandError('JSON data has no "title" property')
        if not place_data.get('coordinates'):
            raise CommandError('JSON data has no "coordinates" property')

        try:
            lat = float(place_data['coordinates']['lat'])
        except KeyError:
            raise CommandError('Latitude is not specified')
        except TypeError:
            raise CommandError('Latitude is not a valid float number')

        try:
            lng = float(place_data['coordinates']['lng'])
        except KeyError:
            raise CommandError('Longitude is not specified')
        except TypeError:
            raise CommandError('Longitude is not a valid float number')

        # Check and substitute for the lack of descriptions

        description_short = place_data.get('description_short')
        if not description_short:
            description_short = 'Нет описания'
            self.stdout.write(self.style.WARNING('Short description plugged for lack of value'))

        description_long = place_data.get('description_long')
        if not description_long:
            description_long = 'Нет описания'
            self.stdout.write(self.style.WARNING('Long description plugged for lack of value'))

        # Create new place if it doesn't already exist

        new_place, created = Place.objects.get_or_create(
            title=title,
            defaults={
                'lat': lat,
                'lng': lng,
                'description_short': description_short,
                'description_long': description_long
            })
        if not created:
            self.stdout.write(self.style.ERROR(f'Place "{title}" already exist in DB.'))
            return

        self.stdout.write(f'"{title}" added to DB...')

        # Load and add images

        self.stdout.write(f'Loading images related to "{title}"...')

        for index, img_url in enumerate(place_data.get('imgs')):
            img_filename = urlsplit(img_url).path.split("/")[-1]

            try:
                response = requests.get(img_url)
                response.raise_for_status()
            except requests.HTTPError as err:
                self.style.WARNING(f'Failed to fetch image {img_url}')
                self.style.WARNING(err)
                continue

            img_file = ImageFile(BytesIO(response.content))

            new_image = new_place.images.create()
            new_image.img_file.save(img_filename, img_file, save=False)
            new_image.index = index + 1
            new_image.save()

            self.stdout.write(f'{img_filename} added to "{title}"...')

        self.stdout.write(self.style.SUCCESS(f'Place "{title}" is loaded completely! :D'))


    def handle(self, *args, **options):
        source = str(kwargs['source'])
        if os.path.isfile(source):
            with open(source, 'r') as file:
                list_of_links = file.readlines()
            for link in list_of_links:
                self.fill_data_from_link(link)

        else:
            self.fill_data_from_link(source)
