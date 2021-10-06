from django.db import models

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    location = models.PointField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True )
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name