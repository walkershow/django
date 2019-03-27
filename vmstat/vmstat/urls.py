"""vmstat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from vmapi.views import GetTasklistView
from vmapi.views import js, css, home
from django.shortcuts import render
from django.http import HttpResponse


def list(request):
    return HttpResponse("hello worldh")


urlpatterns = [
    # path("admin/", admin.site.urls),
    # url("^blog/", include(("blog.urls", "blog"), namespace="blog")),
    url("^vmapi/", include("vmapi.urls")),
    url(r"^$", home, name="index"),  # 访问 js 文件，记得，最后没有 /
    url(r"^js/(?P<filename>.*\.js)$", js, name="js"),  # 访问 js 文件，记得，最后没有 /
    url(r"^css/(?P<filename>.*\.css)$", css, name="css"),  # 访问 css 文件，记得，最后没有 /
]
# # urlpatterns = [url(r"^vmapi/", include("vmapi.urls"))]
# urlpatterns = [url("^hi/", list, name="home")]
# print(urlpatterns)
# # urlpatterns = [url(r"^vmapi/", list)]
# print(GetTasklistView)
# # urlpatterns = [url("^vmapi/", GetTasklistView.as_view(), name="index")]
# print(include("vmapi.urls"))
