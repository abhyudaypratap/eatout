"""View for Search Api."""
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers
import json

from .serializers import RestaurantSerializer
from .models import Restaurantdb
from restaurant import search


class RestaurantSearchApiView(APIView):
    """Restaurant Search Api."""
    renderer_classes = (JSONRenderer, )

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
        res_data = RestaurantSerializer(data=request.data)
        if res_data.is_valid():
            res_data.save()
            return Response(res_data.data, status=status.HTTP_200_OK)


class RestaurantsDataView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        res_data = serializers.serialize("json", Restaurantdb.objects.all())
        return Response(json.loads(res_data), status=status.HTTP_200_OK)

# class RestaurantApiView(APIView):

#     def post(self, request, *args, **kwargs):

#         review = request.data.get("coordinates")
#         user = request
