from django.contrib import admin
from .models import *

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ("author",)
    list_display = ("title", "author", "publish", "status")
    search_fields = ("title", "body")
    list_filter = ("author", "publish", "status")
    date_hierarchy = "publish"


admin.site.register(Post, PostAdmin)
