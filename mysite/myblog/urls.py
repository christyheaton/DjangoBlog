from django.conf.urls import url
from myblog.views import stub_view
from myblog.views import list_view

urlpatterns = [
    url(r'^$', list_view, name="blog_index"),
    url(r'^posts/(\d+)/$', stub_view, name="blog_detail"),
]
