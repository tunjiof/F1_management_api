from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("regular", "Regular")
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=False, null=False)
    last_name = models.CharField(max_length=40, blank=False, null=False)
    role = models.CharField(max_length=40, choices=ROLE_CHOICES, blank=False, null=False, default="regular")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
