from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status="published")


class Post(models.Model):
    STATUS_CHOICES = (("draft", "草稿"), ("published", "发布"))
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date="publish")
    author = models.ForeignKey(User, related_name="blog_posts", on_delete="CASSADE")
    body = models.TextField()
    publish = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    published = PublishManager()

    def __str__(self):
        return self.title
