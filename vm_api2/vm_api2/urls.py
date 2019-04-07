"""vm_api2 URL Configuration

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
from rest_framework.routers import DefaultRouter
from backend.views import TaskViewSet, home, js, css

router = DefaultRouter()
router.register(prefix="task", viewset=TaskViewSet, base_name="task")
API_V1 = []
API_V1.extend(router.urls)
API_VERSION = [url(r"^v1/", include(API_V1))]
urlpatterns = [
    url(r"^api/", include(API_VERSION)),
    url(r"^admin/", admin.site.urls),
    url(r"^js/(?P<filename>.*\.js)$", js, name="js"),
    url(r"^css/(?P<filename>.*\.css)$", css, name="css"),
    url(r"^$", home, name="home"),
]
