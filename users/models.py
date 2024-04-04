from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True,null=True,verbose_name='Photo')
    date_birth = models.DateField(blank=True,null=True,verbose_name='Date of Birth')