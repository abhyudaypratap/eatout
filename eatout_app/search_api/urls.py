from django.conf.urls import include, url
from search_api import views


urlpatterns = [
    url(r'^restaurant/', views.RestaurantSearchApiView.as_view(), name="restaurant_search"),
]
