from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    user_image = models.ImageField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    passport_id = models.CharField(max_length=230, null=True)
    visa_number = models.CharField(123, null=True)
    COUNTY_CHOICES = [
        ('US', 'United States'),
        ('CA', 'Canada'),
        ('UK', 'United Kingdom'),
        ('AU', 'Australia'),
        ('UZ', 'UZBEKISTAN'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('JP', 'Japan'),
        ('BR', 'Brazil'),
        ('MX', 'Mexico'),
        ('CN', 'China'),
        ('IN', 'India'),
        ('ZA', 'South Africa'),
    ]
    county = models.CharField(max_length=2, choices=COUNTY_CHOICES, null=True)
    ganders = [
        ('M', 'male'),
        ('F', 'famele'),
    ]
    gander = models.CharField(max_length=1 , choices=ganders , null=True)

