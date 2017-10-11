from rest_framework import serializers
from .models import Restaurantdb, RestaurantReviews


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurantdb
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReviews
        fields = '__all__'