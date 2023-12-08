from django.db import models


class Artists(models.Model):

    class Meta:
        verbose_name_plural = 'Artists'

    artist = models.CharField(max_length=254, null=True, blank=True)
    profile_info = models.TextField()

    def __str__(self):
        return self.artist
