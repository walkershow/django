import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin  # Create your models here.
from django.urls import reverse

VIEWABLE_STATUS = [3, 4]


class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)


class Category(models.Model):
    label = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.label


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("label",)}


class Story(models.Model):
    STATUS_CHOICES = (
        (1, "need edit"),
        (2, "need approval"),
        (3, "published"),
        (4, "archived"),
    )

    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete="CASSADE")
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User, on_delete="CASSADE")
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    admin_objects = models.Manager()
    objects = ViewableManager()

    class Meta:
        ordering = ["modified"]
        verbose_name_plural = "stors"

    # @models.permalink
    def get_absoulte_url(self):
        return reverse("cms-story", args=(self.slug,))
        # return ("cms-story", None, {"slug": self.slug})


class StoryAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status")
    search_fileds = ("title", "content")
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Story, StoryAdmin)
admin.site.register(Category, CategoryAdmin)
