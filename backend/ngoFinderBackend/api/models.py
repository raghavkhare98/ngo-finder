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

"""
CREATE TABLE api_city(
  id INT, 
  city_name VARCHAR(255) UNIQUE
  );

INSERT INTO api_city(id, city_name) VALUES(1, 'city1');
INSERT INTO api_city(id, city_name) VALUES(2, 'city2');
INSERT INTO api_city(id, city_name) VALUES(3, 'city3');
INSERT INTO api_city(id, city_name) VALUES(4, 'city4');

SELECT * FROM api_city;

CREATE TABLE api_ngo(
  ngo_id INT, 
  ngo_desc VARCHAR(255), 
  ngo_city_name VARCHAR(255) REFERENCES api_city (city_name)
  );


INSERT INTO api_ngo(ngo_id, ngo_desc, ngo_city_name) 
  SELECT 
    1,
    'desc',
    city_name
  FROM
    api_city;

SELECT * FROM api_ngo;
"""