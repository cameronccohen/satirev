from django.conf.urls import url
from articles.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
]