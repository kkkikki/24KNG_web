from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail_url = models.URLField()
    video_url = models.URLField()

    def __str__(self):
        return self.title
