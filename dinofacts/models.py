from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

class Profile(models.Model):
    dinosor = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.dinosor
# Create your models here.
