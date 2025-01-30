from rest_framework import serializers
from .models import City, NGO

#we are using model serializers because we want to serialize data directly from django models
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class NGOSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = '__all__'