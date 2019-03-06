from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .models import BlogPost
from django.template import loader, Context

# Create your views here.


def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("index.html")
    print(posts[0].title)
    c = Context({"posts": posts})
    print(c)
    html = t.render({"posts": posts})
    return HttpResponse(html)
    # print(QueryDict(request.body))
    # return HttpResponse("hello world")
    # return HttpResponse(qs[0].title)
