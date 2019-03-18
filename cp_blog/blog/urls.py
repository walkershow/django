from django.conf.urls import url
from . import views

urlpatterns = [
    # url("^$", views.post_list, name="post_list"),
    url("^$", views.PostListView.as_view(), name="post_list"),
    url(r"^tag/(?P<tag_slug>[-\w]+)/$", views.post_list, name="post_list_by_tag"),
    url(
        r"^(?P<y>\d{4})/(?P<m>\d{2})/(?P<d>\d{2})/(?P<post>[-\w]+)/$",
        views.post_detail,
        name="post_detail",
    ),
]
