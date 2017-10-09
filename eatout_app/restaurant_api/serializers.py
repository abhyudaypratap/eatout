from rest_framework import serializers
from .models import Restaurantdb


class AddRestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurantdb
        fields = '__all__'