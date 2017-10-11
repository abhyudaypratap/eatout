from rest_framework import serializers
from .models import Restaurantdb, RestaurantReviews, ReviewsComments


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurantdb
        fields = '__all__'


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantReviews
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReviewsComments
        fields = '__all__'