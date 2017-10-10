from django.conf.urls import include, url
from restaurant_api import views


urlpatterns = [
    url(r'^search/', views.RestaurantSearchApiView.as_view(), name="restaurant_search"),
    url(r'^add/', views.AddRestaurantApiView.as_view(), name="new_restaurant"),
    url(r'^data/', views.RestaurantsDataView.as_view(), name="restaurants"),
]
