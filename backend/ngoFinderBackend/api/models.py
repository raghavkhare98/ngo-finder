from django.db import models

class City(models.Model):
    #TODO: Add a zip code field in the City model class
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
class NGO(models.Model):

    ngo_name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='ngos')
    #will also have to create an event date column here

    def __str__(self):
        return self.name