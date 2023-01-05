from django.db import models

from mainapp.models import User


class Remember(models.Model):
    """ Remember Model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    create_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_timestamp']
        unique_together = ('latitude', 'longitude')

    def __str__(self):
        return self.title
