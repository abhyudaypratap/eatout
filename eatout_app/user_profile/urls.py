from django.conf.urls import include, url
from user_profile import views


urlpatterns = [
    url(r'^details/', views.UserDetailsView.as_view(), name="User"),
]
