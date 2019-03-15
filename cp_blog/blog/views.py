from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, "blog/post/list.html", {"posts": posts})


def post_detail(request, y, m, d, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=y,
        publish__month=m,
        publish_day=d,
    )
    return render(request, "blog/post/detail.html", {"post": post})
