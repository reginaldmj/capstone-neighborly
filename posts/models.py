from django.db import models
from django.utils import timezone
from neighborly.models import NeighborlyUser

class Post(models.Model):
    body = models.TextField()
    time_stamp = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(NeighborlyUser, on_delete=models.CASCADE, related_name='user_tweeted')
