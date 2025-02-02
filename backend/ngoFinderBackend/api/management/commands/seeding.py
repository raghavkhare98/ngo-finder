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

def clear_data():
    logging.info('Clearing/Deleting data objects')
    NGO.objects.all().delete()
    City.objects.all().delete()

def create_ngos():
    logging.info('Creating data objects')
    cities = ['Waterloo', 'Kitchener', 'Cambridge', 'Guelph']
    ngos = NGO(
        ngo_name=fake.name(),
        description=fake.text(),
        city_name=random.choice(cities)
    )
    ngos.save()
    logging.info('Creation complete')
    return ngos

    
def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return
    for _ in range(20):
        create_ngos()
