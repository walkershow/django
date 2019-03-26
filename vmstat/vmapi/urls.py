from django.conf.urls import url, include

# from .views import GetTasklistView
from . import views

urlpatterns = [url(r"^$", views.GetTasklistView.as_view(), name="hh")]
