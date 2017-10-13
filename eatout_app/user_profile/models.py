from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserDetail(models.Model):

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number \
    must be entered in the format: '+999999999'. Up to 12 digits allowed.")

    user = models.OneToOneField(User, unique=True, blank=False, null=False)
    contact = models.CharField(
        validators=[phone_regex], blank=True, max_length=15)  # validators should be a list
    company_name = models.CharField(max_length=100, blank=False, null=False)
    profile_pic = models.ImageField(default='user.png')

    def __unicode__(self):
        return self.user.username