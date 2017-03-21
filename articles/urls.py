from django.conf.urls import url
from articles.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^articles/(?P<slug>[a-zA-Z\d_\-]+)/$', article, name='article'),
]