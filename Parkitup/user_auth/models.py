from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class MyUser(AbstractUser):
    mobile_num = PhoneNumberField(region="IN")
    mobile_verified= models.BooleanField(default = False)
    dl_number = models.CharField(
        max_length=16,  # Max length to accommodate patterns like "DL14 20110012345"
        blank=True,  # Optional field; set to False if mandatory
        null=True,
        validators=[
            RegexValidator(
                regex=r"^DL-\d{2}\d{11}$|^DL\d{2}\s\d{11}$",
                message="DL number must follow the pattern 'DL-1420110012345' or 'DL14 20110012345'.",
            )
        ],
        help_text="Enter your driving license number in the format 'DL-1420110012345' or 'DL14 20110012345'.",
    )
    dl_verified = models.BooleanField(default=False)

    