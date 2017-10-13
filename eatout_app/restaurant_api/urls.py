from django.conf.urls import include, url
from restaurant_api import views

app_name = 'api'
urlpatterns = [
    url(r'^search/', views.RestaurantSearchApiView.as_view(), name="restaurant_search"),
    url(r'^add/', views.AddRestaurantApiView.as_view(), name="new_restaurant"),
    url(r'^visited/', views.VistedRestaurantsApiDataView.as_view(), name="visited_restaurants"),
    url(r'^visit/', views.VistedRestaurantsStoreApiView.as_view(), name="visited_restaurant_save"),
    url(r'^list/', views.RestaurantsListApiView.as_view(), name="restaurants_list"),
    url(r'^down/', views.VoteDownApiView.as_view(), name="vote_down"),
    url(r'^display/(?P<slug>.+)/', views.RestaurantDataApiView.as_view(), name="restaurant_info"),
]
