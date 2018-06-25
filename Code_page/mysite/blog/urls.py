from django.conf.urls import include, url
from . import views 


urlpatterns = [
        url('^$', views.post_list, name = "buscar"),
]
