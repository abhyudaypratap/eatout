"""Google Places Api."""
import re
import requests
from settings.common import google_key


def get_image_url(ref, h, w):
    """
    Input:
        Photoreference id
        Width and Height of Image
    Output:
        Returns concatenated url with width and height
    """
    if ref:
        s_url = "https://maps.googleapis.com/maps/api/place/photo?maxheight=" \
            + str(h) + "&maxwidth=" + str(w) + \
            "&photoreference=" + ref + "&key=" + google_key
        return s_url
    else:
        return ""


def crestaurantlist(r_data):
    """
    Input:
        Restaurant list obtained from google place api using coordinates
    Output:
        Returns a list of dict with properties of restaurant
    """
    l_data = []
    restaurant_data = {}
    image = ""
    rat = ""
    for data in r_data:
        if "photos" in data:
            image = get_image_url(data["photos"][0]["photo_reference"], data[
                "photos"][0]["height"], data["photos"][0]["width"])
        if "rating" in data:
            rat = data["rating"]
        restaurant_data = {
            "id": data["id"],
            "name": data["name"],
            "location": data["geometry"]["location"],
            "address": data["vicinity"],
            "rating": rat,
            "image": image,
        }
        l_data.append(restaurant_data)
    return l_data


def qrestaurantlist(r_data):
    """
    Input:
        Restaurant list obtained from google place api using text
    Output:
        Returns a list of dict with properties of restaurant
    """
    l_data = []
    restaurant_data = {}
    image = ""
    rat = ""
    for data in r_data:
        if "photos" in data:
            image = get_image_url(data["photos"][0]["photo_reference"], data[
                "photos"][0]["height"], data["photos"][0]["width"])
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
            "image": image,
        }
        l_data.append(restaurant_data)
    return l_data


def searchbycordinates(coordinates):
    """Searching a restaurant using User provide latitude and longtiude
    Searching using Google Places API Web Service
    Input:
        Latitude and Longtitude of a location
    Output:
        List of dict with restaurtants  information
    """
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + \
        coordinates + "&opennow=true&rankby=distance&types=restaurant&key=" + google_key
    search_data = requests.get(url)
    res_list = search_data.json()["results"]
    res_data = crestaurantlist(res_list)
    restaurant_data = {"data": res_data}
    return restaurant_data


def searchbyquery(query, coordinates):
    """Searching a restaurant using User query
    Searching using Google Places API Web Service
    Input:
        Text: query made by user
    Output:
        List of dict with restaurtants  information
    """
    loc = ""
    if coordinates:
        loc = "&location=" + coordinates
    query = re.sub(r"\s+", '+', query)
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + \
        query + loc + "&types=restaurant&key=" + google_key
    search_data = requests.get(url)
    res_list = search_data.json()["results"]
    res_data = qrestaurantlist(res_list)
    restaurant_data = {"data": res_data}
    return restaurant_data
