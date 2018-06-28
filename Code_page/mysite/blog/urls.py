from django.conf.urls import include, url
from . import views


urlpatterns = [
        url('^$', views.post_list, name = "buscar"),
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
