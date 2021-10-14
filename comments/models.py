from django.db import models
from django.utils import timezone
from neighborlyUsers.models import NeighborlyUser

class Comment(models.Model):
    image = models.ImageField(
      upload_to='images/', blank=True,)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    user = models.ForeignKey(NeighborlyUser, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.content