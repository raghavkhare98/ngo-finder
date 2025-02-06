from rest_framework import generics
from .models import City, NGO
from .serializers import CitySerializer, NGOSerializer

class CityListCreate(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class NGOListCreate(generics.ListCreateAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

class NGOsByCity(generics.ListAPIView):

    serializer_class = NGOSerializer

    def get_queryset(self):
        city_name = self.kwargs['city_name']
        return NGO.objects.filter(ngo_city_name__city_name=city_name)