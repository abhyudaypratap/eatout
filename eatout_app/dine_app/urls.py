from django.conf.urls import url
from dine_app import views

app_name = 'restaurant'
urlpatterns = [
    url(r'^search/', views.RestaurantSearchView.as_view(), name="restaurant_search"),
    url(r'^add/', views.AddRestaurantView.as_view(), name="new_restaurant"),
    url(r'^visited/', views.VistedRestaurantsDataView.as_view(), name="visited_restaurants"),
    url(r'^visit/', views.VistedRestaurantsStoreView.as_view(), name="visited_restaurant_save"),
    url(r'^list/', views.RestaurantsListView.as_view(), name="restaurants_list"),
    url(r'^down/', views.VoteDownView.as_view(), name="vote_down"),
    url(r'^display/(?P<slug>.+)/', views.RestaurantDataView.as_view(), name="restaurant_info"),
]
