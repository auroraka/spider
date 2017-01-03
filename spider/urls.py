"""spider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
	url(r'^test','keke.views.test',name='test'),
	url(r'^notfound','keke.views.notfound',name='notfound'),
	url(r'^base','keke.views.base',name='base'),
	url(r'^login','keke.views.login',name='login'),
	url(r'^register','keke.views.register',name='register'),
    url(r'^search/?$','keke.views.searchIndex',name='searchIndex'),
    url(r'^search/([^/]+)/?$','keke.views.search',name='search'),
    url(r'^search/([^/]+)/([^/]+)/?$','keke.views.to_searchPage',name='to_searchPage'),
    url(r'^search/([^/]+)/([^.]+)/([^/]+)/?$','keke.views.searchPage',name='searchPage'),
    url(r'^home|index','keke.views.index',name='index'),
    url(r'^admin', include(admin.site.urls)),
	url(r'^$','keke.views.index',name='index'),
    #url(r'[\s\S]*','keke.views.notfound',name='notfound'),
    url(r'[\s\S]*','keke.views.to_notfound',name='to_notfound'),
    #url(r'[\s\S]*', RedirectView.as_view(url='/notfound')),
]

