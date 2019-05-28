"""satirev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import articles

urlpatterns = [
	url(r'^$', include('articles.urls')),
	url(r'^article/(?P<slug>[a-zA-Z\d_\-]+)/$', articles.views.article, name='article'),
	url(r'^section/(?P<section>[a-zA-Z\d_\-]+)/$', articles.views.section, name='section'),
    url(r'^about/', articles.views.about, name='about'),
    url(r'^advertising/', articles.views.advertising, name='advertising'),
    url(r'^subscribe/', articles.views.subscribe, name='subscribe'),
    url(r'^tag/(?P<tag>[a-zA-Z\d_\-]+)/$', articles.views.tag, name='tag'),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admin/', admin.site.urls),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#PRODTODO HAVE TO DELETE THE ABOVE static part for production!!
#https://docs.djangoproject.com/en/1.10/howto/static-files/deployment/