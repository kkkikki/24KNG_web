from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/')
    cloudfront_url = models.URLField()
# Create your models here.
