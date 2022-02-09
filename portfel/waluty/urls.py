from django.urls import path #import bibliotek odpowiedzialnej za ścieżki :D
from .views import *  # import wszystkich widoków z pliku views

urlpatterns = [
    path('', index, name='index'),
    path('eth/', eth, name='eth'),
    path('btc/', btc, name='btc'),
    path('ltc/', ltc, name='ltc'),
    path('bnb/', bnb, name='bnb'),
    path('sol/', sol, name='sol'),
    path('ada/', ada, name='ada'),
    path('xrp/', xrp, name='xrp'),
    path('busd/', busd, name='busd'),
    path('atom/', atom, name='atom'),
]
