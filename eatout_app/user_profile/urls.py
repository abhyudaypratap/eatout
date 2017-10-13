from django.conf.urls import include, url
from user_profile import views

app_name = 'user'

urlpatterns = [
    url(r'^details/', views.UserDetailsView.as_view(), name="user_data"),
]
