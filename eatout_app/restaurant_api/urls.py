from django.conf.urls import include, url
from restaurant_api import views

app_name = 'restaurant'
urlpatterns = [
    url(r'^search/', views.RestaurantSearchApiView.as_view(), name="restaurant_search"),
    url(r'^result/', views.SearchResultApiView.as_view(), name="results"),
    url(r'^add/', views.AddRestaurantApiView.as_view(), name="new_restaurant"),
    url(r'^visited/', views.VistedRestaurantsDataView.as_view(), name="visited_restaurants"),
    url(r'^list/', views.RestaurantsListView.as_view(), name="restaurants_list"),
    url(r'^display/(?P<slug>.+)/', views.RestaurantDataView.as_view(), name="restaurant_info"),
]
