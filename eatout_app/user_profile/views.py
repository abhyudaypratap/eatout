"""View for UserProfile."""
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserDetail


class UserDetailsView(LoginRequiredMixin, APIView):
    """Restaurant Search Api."""
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer, ]
    template_name = 'userprofile/user_data.html'

    def get(self, request):
        user = UserDetail.objects.get(user=request.user)
        data = {"user": user}
        return Response(data, status=status.HTTP_200_OK)
