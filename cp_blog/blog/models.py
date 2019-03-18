from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

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
    objects = models.Manager()
    published = PublishManager()
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail",
            args=[
                self.publish.year,
                self.publish.strftime("%m"),
                self.publish.strftime("%d"),
                self.slug,
            ],
        )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete="CASSADE")
    name = models.CharField(max_length=50)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "comment by {} on {}".format(self.name, self.post)
