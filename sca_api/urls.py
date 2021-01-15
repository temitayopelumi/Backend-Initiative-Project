from .views import Users, Movies, Rentals
from django.urls import path

urlpatterns = [
    path('users/', Users, name='user'),
    path('movies/', Movies, name='movie'),
    path('rentals/', Rentals, name='rental'),
]