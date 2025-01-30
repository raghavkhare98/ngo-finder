from django.urls import path

from views import CityListCreate, NGOListCreate, NGOsByCity

urlPatterns = [
    path("cities/", CityListCreate.as_view(), name="city-list"),
    path("ngos/", NGOListCreate.as_view(), name="ngo-list"),
    path("ngos/<str:city_name>/", NGOsByCity.as_view(), name="ngos-by-city")
]