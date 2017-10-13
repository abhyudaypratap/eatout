"""View for Search Api."""
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

import json

from .serializers import RestaurantSerializer, ReviewsSerializer, CommentsSerializer
from .models import Restaurantdb
from restaurant import search


class RestaurantSearchApiView(APIView):
    """Restaurant Search Api."""
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer, ]
    template_name = 'restaurant/search.html'

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        coordinates = request.data.get("coordinates")
        query = request.data.get("query")
        if query and coordinates:
            result = search.searchbyquery(query, coordinates)
            return Response(result)
        elif query:
            result = search.searchbyquery(query, coordinates)
            return render(request, 'restaurant/result.html', {"result": result['data']})
            # return Response(result)
        elif coordinates:
            result = search.searchbycordinates(coordinates)
            return Response(result)
        else:
            return Response({"data": "no data send"})


class SearchResultApiView(APIView):
    """Restaurant Search Result Api."""
    # renderer_classes = [TemplateHTMLRenderer, JSONRenderer, ]
    # template_name = 'restaurant/result.html'

    def get(self, request, *args):
        return Response(status=status.HTTP_200_OK)


class AddRestaurantApiView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        if Restaurantdb.objects.filter(restaurant_id=data["restaurant_id"]).exists():
            return HttpResponse("Restaurant already added")
        else:
            res_data = RestaurantSerializer(data=data)
            if res_data.is_valid():
                res_data.save()
                return HttpResponseRedirect(reverse("restaurant:restaurants_list"))


class VistedRestaurantsDataView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/visited.html'

    def get(self, request):
        res_data = serializers.serialize("json", Restaurantdb.objects.all())
        restaurants = {"restaurants": json.loads(res_data)}
        return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantsListView(APIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/visited.html'

    def get(self, request):
        res_data = serializers.serialize("json", Restaurantdb.objects.all())
        restaurants = {"restaurants": json.loads(res_data)}
        return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantDataView(LoginRequiredMixin, APIView):
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/place_display.html'

    def get(self, request, slug):
        restaurant = Restaurantdb.objects.get(restaurant_id=slug)
        data = {"restaurant": restaurant}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        data = request.data.copy()
        data["registered_user"] = request.user.pk
        if "comments" in data:
            rev_data = CommentsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return HttpResponseRedirect(reverse("restaurant:restaurant", args=[slug]))
        else:
            data["restaurant"] = slug
            rev_data = ReviewsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return HttpResponseRedirect(reverse("restaurant:restaurant", args=[slug]))


# class RestaurantApiView(APIView):

#     def post(self, request, *args, **kwargs):

#         review = request.data.get("coordinates")
#         user = request
