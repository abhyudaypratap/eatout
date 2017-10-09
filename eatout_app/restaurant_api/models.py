from django.db import models
from django.contrib.auth.models import User
import uuid


class Restaurantdb(models.Model):
    restaurant_id = models.CharField(max_length=225, primary_key=True)
    name = models.CharField(max_length=225, null=False, blank=False)
    geocode = models.CharField(max_length=225, null=False, blank=False)
    address = models.CharField(max_length=225, null=True, blank=True)
    image_url = models.CharField(max_length=525, null=True, blank=True)
    visted = models.IntegerField(default=0)
    google_rating = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        """Return Restaurant Id."""
        return str(self.restaurant_id)
