
from django.db import models




# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True )
    address = models.CharField(max_length=150, blank=True, null=True )
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return self.name
