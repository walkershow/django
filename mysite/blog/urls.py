from django.conf.urls import url
from .views import archive

urlpatterns = [url("^$", archive)]
