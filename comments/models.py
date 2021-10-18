from django.db import models
from django.utils import timezone
from neighborlyUsers.models import NeighborlyUser
from posts.models import Post


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', null=True)
    posted_by = models.ForeignKey(
        NeighborlyUser, on_delete=models.CASCADE, related_name='user_commented', null=True)
    body = models.TextField(null=True)
    created_on = models.DateTimeField(default=timezone.now, null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.body
