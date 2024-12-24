from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

class CustomUser(AbstractUser):
    mobile_num = PhoneNumberField(region="IN")
    mobile_verified= models.BooleanField(default = False)