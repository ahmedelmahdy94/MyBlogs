from __future__ import unicode_literals
from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    """docstring for Post."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    update = models.DateField(auto_now=True, auto_now_add=False)
    create_date = models.DateField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return f"/post/{self.id}"

    def __str__(self):
        return self.title
