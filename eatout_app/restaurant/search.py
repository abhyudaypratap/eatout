"""Google Places Api """
import re
import requests
from settings.common import google_key


def crestaurantlist(r_data):
    l_data = []
    restaurant_data = {}
    for data in r_data:
        if "rating" in data:
            rat = data["rating"]
        else:
            rat = ""
        restaurant_data = {
            "id": data["id"],
            "name": data["name"],
            "location": data["geometry"]["location"],
            "address": data["vicinity"],
            "rating": rat,
        }
        l_data.append(restaurant_data)
    return l_data


def qrestaurantlist(r_data):
    l_data = []
    restaurant_data = {}
    for data in r_data:
        if "rating" in data:
            rat = data["rating"]
        else:
            rat = ""
        restaurant_data = {
            "id": data["id"],
            "name": data["name"],
            "location": data["geometry"]["location"],
            "address": data["formatted_address"],
            "rating": rat,
        }
        l_data.append(restaurant_data)
    return l_data


def searchbycordinates(coordinates):
    """Searching a restaurant using User provide latitude and longtiude"""
    # Searching using Google Places API Web Service
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + \
        coordinates + "&opennow=true&rankby=distance&types=restaurant&key=" + google_key
    search_data = requests.get(url)
    res_list = search_data.json()["results"]
    res_data = crestaurantlist(res_list)
    restaurant_data = {"data": res_data}
    return restaurant_data


def searchbyquery(query, coordinates):
    """Searching a restaurant using User provide latitude and longtiude"""
    # Searching using Google Places API Web Service
    loc = ""
    if coordinates:
        loc = "&location=" + coordinates
    query = re.sub(r"\s+", '+', query)
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + \
        query + loc + "&opennow=true&types=restaurant&key=" + google_key
    print url
    search_data = requests.get(url)
    res_list = search_data.json()["results"]
    res_data = qrestaurantlist(res_list)
    restaurant_data = {"data": res_data}
    return restaurant_data
