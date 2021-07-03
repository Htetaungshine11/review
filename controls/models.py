from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Cuser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.IntegerField(unique=True) 
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = [
        'username','phone_number'
    ]