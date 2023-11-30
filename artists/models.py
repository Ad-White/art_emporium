from django.db import models


class Artists(models.Model):
    artist = models.CharField(max_length=254, null=True, blank=True)
    profile_info = models.TextField()

    def __str__(self):
        return self.artist
