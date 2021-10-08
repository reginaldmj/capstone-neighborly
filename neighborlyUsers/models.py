from django.db import models
from django.contrib.auth.models import AbstractUser
from location.models import Neighborhood

# Create your models here.


class NeighborlyUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(blank=True, null=True)
    posts = models.IntegerField(default=0, blank=True, null=True)
    location = models.ForeignKey(
        Neighborhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username
