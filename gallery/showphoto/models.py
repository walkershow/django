from django.db import models
from django.contrib import admin
from .fields import ThumbnailImageField

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=50)
    # fmt off
    image = ThumbnailImageField(upload_to="photo")
    item = models.ForeignKey(Item, on_delete="CASCADE")
    # fmt on

    def __str__(self):
        return self.title


class PhotoInline(admin.StackedInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
