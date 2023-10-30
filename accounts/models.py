from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
<<<<<<< HEAD
        verbose_name_plural = 'CustomUser'

=======
        verbose_name_plural = 'CustomUser'
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
