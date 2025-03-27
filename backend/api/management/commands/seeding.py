#making the seed file available as a command hence created a management/commands folder structure
from django.core.management.base import BaseCommand
import random
from api.models import NGO, City
import logging
from faker import Faker

MODE_REFRESH = 'refresh' 
MODE_CLEAR = 'clear'
fake = Faker()

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")
    
    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options['mode'])
        self.stdout.write("seeding completed")

cities = ['Waterloo', 'Kitchener', 'Cambridge', 'Guelph']

def clear_data():
    logging.info('Clearing/Deleting data objects')
    NGO.objects.all().delete()
    City.objects.all().delete()

def create_cities():
    for city_name in cities:
        city = City(city_name=city_name)
        city.save()
    logging.info('Created cities')

def create_ngos():
    logging.info('Creating data objects')
    
    rand_city = City.objects.order_by('?').first()

    ngos = NGO(
        ngo_name=fake.company(),  
        ngo_description=fake.text(),
        ngo_city_name=rand_city 
    )
    
    ngos.save()
    logging.info("Created ngo")


def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return clear_data()
    
    create_cities()
    for i in range(10):
        create_ngos()