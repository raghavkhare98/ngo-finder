from faker import Faker
from .models import City, NGO

#we need django because the models and the app itself on which we are writing the mock data on, are part of the django app env
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ngoFinderBackend.settings")
django.setup() 

fake = Faker()

def seed_data():
    cities=["Waterloo", "Kitchener", "Cambridge", "Guelph"]
    city_obj = {name: City.objects.get_or_create(name=name)[0] for name in cities}

    for i in range(20):
        NGO.objects.create(
            ngo_name=fake.company(),
            city=city_obj[fake.random.choice(cities)]
        )
    print("Mock data created")

if __name__=="__main__":
    seed_data()