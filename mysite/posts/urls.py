
from django.urls import path
from django.conf.urls import include, url

from .views import *

urlpatterns = [
      path("", post_list_view),
      path("post/create/", post_create_view),
      path("post/<int:id>/", post_detail_view),
      path("post/<int:id>/delete/", post_delete_view),
      path("post/<int:id>/update/", post_update_view),
  ]
