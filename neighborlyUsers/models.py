from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class NeighborlyUser(AbstractUser):
    homepage = models.URLField(null=True)
    display_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(blank=True, null=True)
    posts = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.username