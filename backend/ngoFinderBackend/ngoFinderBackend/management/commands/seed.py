#making the seed file available as a command hence created a management/commands folder structure
from django.core.management.base import BaseCommand
import random
from api.models import NGO, City

MODE_REFRESH = 'refresh' #refreshes the db by clearing all previous data and creating new addresses
MODE_CLEAR = 'clear' #just clears the data

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")
    
    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options['mode'])
        self.stdout.write("seeding completed")

def clear_data():
    NGO.objects.all().delete()
    City.objects.all().delete()

def create_addresses():
    pass

def run_seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return
    for i in range(20):
        create_addresses()
