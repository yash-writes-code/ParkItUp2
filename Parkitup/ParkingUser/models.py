from django.db import models
from django.core.validators import RegexValidator
from accounts.models import CustomUser
# Create your models here.
class UserProfile(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    dl_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        help_text="Driving license number",
        validators=[
            RegexValidator(
                regex=r"^DL-\d{2}\d{11}$|^DL\d{2}\s\d{11}$",
                message="DL number must follow the pattern 'DL-1420110012345' or 'DL14 20110012345'."
            )
        ]
    )
    dl_verified=models.BooleanField(default=False)


    