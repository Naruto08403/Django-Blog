from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

def extract_youtube_id(url):
    """Extract YouTube video ID from various YouTube URL formats."""
    patterns = [
        r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def validate_youtube_url(value):
    """Validate YouTube URL."""
    if not value:
        return
    
    video_id = extract_youtube_id(value)
    if not video_id:
        raise ValidationError('Please enter a valid YouTube URL')

class VlogPost(models.Model):
    title = models.CharField(max_length=200)
    video_url = models.URLField(
        validators=[validate_youtube_url],
        help_text="Enter a YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID)"
    )
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=200, blank=True,
        help_text="Enter tags separated by spaces")

    def get_embed_url(self):
        """Get the embedded URL for the YouTube video."""
        video_id = extract_youtube_id(self.video_url)
        if video_id:
            return f'https://www.youtube.com/embed/{video_id}'
        return None

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
