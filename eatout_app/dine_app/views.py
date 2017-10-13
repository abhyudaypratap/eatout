"""View for Search Api."""
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
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
from restaurant_api.models import Restaurantdb, VisitedRes
from restaurant import search


class RestaurantSearchView(APIView):
    """Restaurant Search View."""

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
            return render(request, 'restaurant/result.html', {"result":
                                                              result['data']})
        elif coordinates:
            result = search.searchbycordinates(coordinates)
            return Response(result)
        else:
            return Response({"data": "no data send"})


class AddRestaurantView(APIView):
    """Add a new restautrant from search result to our database."""

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
    """List out all the Restaurant visited by the user."""
    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/visited.html'

    def get(self, request):
        # Displaying only restaurants marked visited by users
        data = Restaurantdb.objects.filter(visted__gt=0, user_rated__gt=0)
        if data:
            res_data = serializers.serialize("json", data)
            restaurants = {"restaurants": json.loads(res_data)}
            return Response(restaurants, status=status.HTTP_200_OK)
        else:
            return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantsListView(APIView):
    """Display all the restaurant added into database by user."""

    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/list.html'

    def get(self, request):
        # user is able check all the restaurants
        res_data = serializers.serialize("json", Restaurantdb.objects.all())
        restaurants = {"restaurants": json.loads(res_data)}
        return Response(restaurants, status=status.HTTP_200_OK)


class RestaurantDataView(LoginRequiredMixin, APIView):
    """Api outputs all the data about the restaurant stored in database."""

    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/place_display.html'

    def get(self, request, slug):
        restaurant = Restaurantdb.objects.get(restaurant_id=slug)
        data = {"restaurant": restaurant}
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, slug):
        # stores user reviews and comments
        data = request.data.copy()
        data["registered_user"] = request.user.pk
        if "comments" in data:
            rev_data = CommentsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return HttpResponseRedirect(reverse("restaurant:restaurant_info", args=[slug]))
        else:
            data["restaurant"] = slug
            rev_data = ReviewsSerializer(data=data)
            if rev_data.is_valid():
                rev_data.save()
                return HttpResponseRedirect(reverse("restaurant:restaurant_info", args=[slug]))


class VistedRestaurantsStoreView(LoginRequiredMixin, APIView):
    """Record the user response of visiting the restaurant."""

    renderer_classes = [TemplateHTMLRenderer, ]
    template_name = 'restaurant/visited.html'

    def post(self, request):
        res_data = Restaurantdb.objects.get(
            restaurant_id=request.data.get("r_id"))
        data = VisitedRes.objects.get_or_create(
            registered_user=request.user, restaurant=res_data, defaults={"visted": 1})
        res_data.visted = res_data.visted + 1
        res_data.save()
        if not data[1]:
            data[0].visted = data[0].visted + 1
            data[0].save()
        return HttpResponseRedirect(reverse("restaurant:restaurant_info", args=[request.data.get("r_id")]))


class VoteDownView(LoginRequiredMixin, APIView):
    """Voting down the restaurant resulting user will not find the restaurants
    again in the list."""

    def post(self, request):
        res_data = Restaurantdb.objects.get(
            restaurant_id=request.data.get("r_id"))
        res_data.user_rated = 0
        res_data.save()
        return HttpResponseRedirect(reverse("restaurant:restaurant_info", args=[request.data.get("r_id")]))
