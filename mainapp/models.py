from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ User Model """
    avatar = models.ImageField(upload_to='images/avatars', blank=True, null=True)
