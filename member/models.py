from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser




class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    phone = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = 'account_profile'
        app_label = 'account'


class CustomUser(AbstractUser):
    phone = models.CharField(
        max_length=100
    )

    REQUIRED_FIELDS = ["email"]


