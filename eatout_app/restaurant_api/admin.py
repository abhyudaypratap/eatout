"""Register your models here."""
from django.contrib import admin
import models

admin.site.register(models.Restaurantdb)
admin.site.register(models.RestaurantReviews)
admin.site.register(models.ReviewsComments)
admin.site.register(models.VisitedRes)
