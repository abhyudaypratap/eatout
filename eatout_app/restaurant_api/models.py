from django.db import models
from django.contrib.auth.models import User
import uuid


class Restaurantdb(models.Model):
    restaurant_id = models.CharField(max_length=225, primary_key=True)
    name = models.CharField(max_length=225, null=False, blank=False)
    geocode = models.CharField(max_length=225, null=False, blank=False)
    address = models.CharField(max_length=225, null=True, blank=True)
    image_url = models.CharField(max_length=525, null=True, blank=True)
    visted = models.IntegerField(default=1)
    google_rating = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        """Return Restaurant Id."""
        return str(self.restaurant_id)


class RestaurantReviews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reviews = models.CharField(max_length=225, null=False, blank=False)
    registered_user = models.ForeignKey(User, related_name='reviews', null=True)
    restaurant = models.ForeignKey(Restaurantdb, related_name='reviews', null=True)
    google_rating = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        """Return email address."""
        return str(self.id)


class ReviewsComments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    registered_user = models.ForeignKey(User, related_name='comments', null=True)
    reviews = models.ForeignKey(RestaurantReviews, related_name='comments', null=True)
    comments = models.CharField(max_length=255)

    def __str__(self):
        """Return email address."""
        return str(self.id)
