from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models


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