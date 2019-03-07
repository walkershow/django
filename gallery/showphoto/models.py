from django.db import models
from django.contrib import admin

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField("photo")
    item = models.ForeignKey(Item, on_delete="CASCADE")

    def __str__(self):
        return self.title


class PhotoInline(admin.StackedInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Photo)
