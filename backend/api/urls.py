from django.urls import path
from .views import CityListCreate, CityNamesView, NGOListCreate, NGOsByCity

#as_view works as a callable for generic views. as_view connects the view class with the url
urlpatterns = [
    path("cities/", CityListCreate.as_view(), name="city-list"),
    path("city-names/", CityNamesView.as_view(), name="city-names"),
    path("ngos/", NGOListCreate.as_view(), name="ngo-list"),
    path("ngos/<str:city_name>/", NGOsByCity.as_view(), name="ngos-by-city")
]