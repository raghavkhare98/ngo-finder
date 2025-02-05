#making the seed file available as a command hence created a management/commands folder structure
from django.core.management.base import BaseCommand
import random
from api.models import NGO, City
import logging
from faker import Faker

MODE_REFRESH = 'refresh' #refreshes the db by clearing all previous data and creating new addresses
MODE_CLEAR = 'clear' #just clears the data
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

def create_city():
    for i in cities:
        city = City(
            city_name=i
        )
        city.save()
    logging.info('City creation complete')
    return city
def create_ngos():
    logging.info('Creating data objects')
    # city = City.objects.order_by('?').first()
    # print(f"Selected city: {city.city_name}") 
    rand_city = City.objects.order_by('?').first() #we used the ? for order by because we want a random object
    ngos = NGO(
        ngo_name=fake.name(),
        ngo_description=fake.text(),
        ngo_city_name=rand_city
    )
    ngos.save()
    logging.info('NGO creation complete')
    return ngos

    
def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return
    
    create_city()
    for _ in range(20):
        create_ngos()
