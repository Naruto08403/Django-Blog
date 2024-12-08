from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class VlogPost(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=200)  # Store tags as comma-separated values

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
