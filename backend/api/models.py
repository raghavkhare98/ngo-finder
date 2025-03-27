from django.db import models

class City(models.Model):
    #TODO: Add a zip code field in the City model class
    city_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.city_name
    
class NGO(models.Model):

    ngo_name = models.CharField(max_length=255)
    ngo_description = models.TextField()
    ngo_city_name = models.ForeignKey(City, on_delete=models.CASCADE, default='string')
    #TODO: Will also have to create an event date column here
    #TODO: Add a link column and provide the homepage's link of the NGO
    def __str__(self):
        return self.ngo_name