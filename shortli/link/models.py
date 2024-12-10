from django.db import models

class ShortenedURL(models.Model):
    short_code = models.CharField(max_length=10, unique=True)
    original_url = models.URLField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    click_count = models.PositiveIntegerField(default=0)

