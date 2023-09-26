import csv
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.db import models


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:
            phone_reader = list(csv.DictReader(csvfile, delimiter=';'))

            for line in phone_reader:
                id, name, image, price, release_date, lte_exists, slug = line.values()
                slug = slugify(name)
                line = Phone(id=id, name=name, image=image, price=price, release_date=release_date,
                              lte_exists=lte_exists, slug=slug)
                line.save()