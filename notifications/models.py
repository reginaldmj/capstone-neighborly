from django.db import models
from neighborlyUsers.models import NeighborlyUser
from posts.models import Post
from datetime import datetime



class Notification(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(NeighborlyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.post
