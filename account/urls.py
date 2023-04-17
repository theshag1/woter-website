from account.views import *
from django.urls import path

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup')

]
