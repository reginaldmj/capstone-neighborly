from django.db import models
from django.utils import timezone
from neighborlyUsers.models import NeighborlyUser

class Post(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    time_stamp = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(NeighborlyUser, on_delete=models.CASCADE, related_name='user_posted')

    def __str__(self):
        return self.body
