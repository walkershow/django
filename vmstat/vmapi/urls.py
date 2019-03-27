from django.conf.urls import url, include

# from .views import GetTasklistView
from . import views

urlpatterns = [
    url(r"^runningstat$", views.GetTasklistView.as_view(), name="hh"),
    url(r"^validtask$", views.GetValidTaskView.as_view(), name="hh2"),
]
