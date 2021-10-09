from django.db import models
from django.utils import timezone
from neighborlyUsers.models import NeighborlyUser

class Post(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    time_stamp = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(NeighborlyUser, on_delete=models.CASCADE, related_name='user_posted')
    likes = models.ManyToManyField(NeighborlyUser, blank=True, related_name='like')
    dislikes = models.ManyToManyField(NeighborlyUser, blank=True, related_name='dislike')
    

    def __str__(self):
        return self.body

    def number_of_likes(self):
        return self.likes
