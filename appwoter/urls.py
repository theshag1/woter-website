from appwoter.views import *
from django.urls import path

urlpatterns = [
    path('', Enterview.as_view(), name='enter'),
    path('home/', CategoryListview.as_view(), name='home'),
    path('home/<int:pk>', Categorys, name='europe'),
    path('travel/', Travelview.as_view(), name='travel'),
    path('travel/<int:pk>', Traveldetil.as_view(), name='detil'),
    path('about/', AboutView.as_view(), name='about')

]
