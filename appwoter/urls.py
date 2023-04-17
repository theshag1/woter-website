from appwoter.views import *
from django.urls import path

urlpatterns = [
    path('', Enterview.as_view(), name='enter'),
    path('home/', Home.as_view(), name='home'),
    path('home/mountain/', mountain.as_view(), name='mountain'),
    path('home/sport/', sport.as_view(), name='sport'),
    path('home/revir/', river.as_view(), name='river'),
    path('home/asia/', asia.as_view(), name='asia'),
    path('home/europe/', europe.as_view(), name='europe'),
    path('travel/', Travelview.as_view(), name='travel'),
    path('travel/<int:pk>', Traveldetil.as_view(), name='detil'),
]
