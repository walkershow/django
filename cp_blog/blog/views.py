from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.views.generic import ListView
from taggit.models import Tag

# Create your views here.
def post_list(request, tag_slug=None):
    posts = Post.published.all()
    posts_all = Post.objects.all()
    paginator = Paginator(posts_all, 3)
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts_all = posts_all.filter(tags__in=[tag])
    page = request.GET.get("page")
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render(
        request, "blog/post/list.html", {"page": page, "posts": posts, "tag": tag}
    )


class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"


def post_detail(request, y, m, d, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status="draft",
        publish__year=y,
        publish__month=m,
        publish__day=d,
    )
    comments = post.comments.filter(active=True)
    if request.method == "POST":
        cf = CommentForm(data=request.POST)
        if cf.is_valid():
            nc = cf.save(commit=False)
            nc.post = post
            nc.save()
    else:
        cf = CommentForm()

    new_comment = None

    return render(
        request,
        "blog/post/detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": cf,
        },
    )
