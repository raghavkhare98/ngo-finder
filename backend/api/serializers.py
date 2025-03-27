from rest_framework import serializers
from .models import City, NGO

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class NGOSerializer(serializers.ModelSerializer):
    
    city_name = serializers.CharField(source='ngo_city_name.city_name', read_only=True)

    class Meta:
        model = NGO
        fields = ['id', 'ngo_name', 'ngo_description', 'city_name']