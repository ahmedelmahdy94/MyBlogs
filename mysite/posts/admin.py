from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    """docstring for PostModelAdmin."""
    list_display = ("title", "update", "create_date")
    list_filter = ("update", "create_date")
    search_fields = ("title", "content")
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
