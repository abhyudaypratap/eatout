from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
import uuid


class Restaurantdb(models.Model):
    restaurant_id = models.CharField(max_length=225, primary_key=True)
    name = models.CharField(max_length=225, null=False, blank=False)
    geocode = models.CharField(max_length=500, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    image_url = models.CharField(max_length=525, null=True, blank=True)
    visted = models.IntegerField(default=0)
    user_rated = models.IntegerField(default=1)
    google_rating = models.CharField(max_length=225, null=True, blank=True)
    contact = models.CharField(max_length=13, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return Restaurant Id."""
        return str(self.restaurant_id)


class RestaurantReviews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    reviews = models.CharField(max_length=3000, null=False, blank=False)
    visted = models.IntegerField(default=0, null=True, blank=True)
    registered_user = models.ForeignKey(User, related_name='reviews', null=True)
    restaurant = models.ForeignKey(Restaurantdb, related_name='reviews', null=True)
    user_rating = models.CharField(max_length=225, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return review Id."""
        return str(self.id)


class ReviewsComments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    registered_user = models.ForeignKey(User, related_name='comments', null=True)
    reviews = models.ForeignKey(RestaurantReviews, related_name='comments', null=True)
    comments = models.CharField(max_length=3000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return comment Id."""
        return str(self.id)


class VisitedRes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    visted = models.IntegerField(default=0, null=True, blank=True)
    registered_user = models.ForeignKey(User, related_name='visited', null=True)
    restaurant = models.ForeignKey(Restaurantdb, related_name='visited', null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return  Id."""
        return str(self.id)
