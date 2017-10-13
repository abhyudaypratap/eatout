"""View for Search Api."""
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers

import json

from .serializers import RestaurantSerializer, ReviewsSerializer, CommentsSerializer
from .models import Restaurantdb, VisitedRes
from restaurant import search


class RestaurantSearchApiView(APIView):
    """Restaurant Search Api."""

    def post(self, request, *args, **kwargs):
        coordinates = request.data.get("coordinates")
        query = request.data.get("query")
        if query and coordinates:
            result = search.searchbyquery(query, coordinates)
            return Response(result)
        elif query:
            result = search.searchbyquery(query, coordinates)
            return Response(result)
        elif coordinates:
            result = search.searchbycordinates(coordinates)
            return Response(result)
        else:
            return Response({"data": "no data send"})


class AddRestaurantApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        if Restaurantdb.objects.filter(restaurant_id=data["restaurant_id"]).exists():
            return Response({"Response": "Restaurant already added"})
        else:
            res_data = RestaurantSerializer(data=data)
            if res_data.is_valid():
                res_data.save()
                return Response(res_data)


class VistedRestaurantsApiDataView(APIView):

    def get(self, request):
        data = Restaurantdb.objects.filter(visted__gt=0, user_rated__gt=0)
        if data:
            res_data = serializers.serialize("json", data)
            restaurants = {"restaurants": json.loads(res_data)}
            return Response(restaurants, status=status.HTTP_200_OK)
        else:
            return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantsListApiView(APIView):

    def get(self, request):
        res_data = serializers.serialize(
            "json", Restaurantdb.objects.filter(user_rated__gt=0))
        restaurants = {"restaurants": json.loads(res_data)}
        return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantDataApiView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request, slug):
        res_data = serializers.serialize(
            "json", Restaurantdb.objects.filter(restaurant_id=slug))
        data = {"restaurant": json.loads(res_data)}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        data = request.data.copy()
        data["registered_user"] = request.user.pk
        if "comments" in data:
            rev_data = CommentsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return Response(data, status=status.HTTP_200_OK)
        else:
            data["restaurant"] = slug
            rev_data = ReviewsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return Response(data, status=status.HTTP_200_OK)


class VistedRestaurantsStoreApiView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        res_data = Restaurantdb.objects.get(
            restaurant_id=request.data.get("restaurant_id"))
        data = VisitedRes.objects.get_or_create(
            registered_user=request.user, restaurant=res_data,
            defaults={"visted": 1})
        res_data.visted = res_data.visted + 1
        res_data.save()
        if not data[1]:
            data[0].visted = data[0].visted + 1
            data[0].save()
            res_data = serializers.serialize(
                "json", [data[0]])
        return Response(json.loads(res_data))


class VoteDownApiView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        res_data = Restaurantdb.objects.get(
            restaurant_id=request.data.get("r_id"))
        res_data.user_rated = 0
        res_data.save()
        res_data = serializers.serialize(
            "json", res_data)
        return Response(json.loads(res_data))
