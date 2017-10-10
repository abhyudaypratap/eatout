from rest_framework import serializers
from .models import Restaurantdb


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurantdb
        fields = '__all__'