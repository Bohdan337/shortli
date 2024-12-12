from django.db import models
from django.contrib.auth.models import User

class ShortenedURL(models.Model):
    short_code = models.CharField(max_length=10, unique=True)
    original_url = models.URLField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    click_count = models.PositiveIntegerField(default=0)

