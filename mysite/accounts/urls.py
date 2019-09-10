from django.urls import path
from django.conf.urls import include, url

from .views import *

urlpatterns = [
      path("login/", login_view),
      path("logout/", logout_view),
      path("signup/", signup_view),
  ]
