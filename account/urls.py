from account.views import *
from django.urls import path

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('change/<int:pk>', UserCHange.as_view(), name='change'),
    path('buy/<int:pk>', UserBUY.as_view(), name='buy'),
    path('addsuccesfly/', add, name='add'),

]
