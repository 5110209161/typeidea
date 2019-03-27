"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from typeidea.custom_site import custom_site

from blog.views import post_list, post_detail
from config.views import links


urlpatterns = [
    #path('admin/', admin.site.urls),
    # url(r'^super_admin/', admin.site.urls),       #硬编码
    # url(r'admin/', custom_site.urls),   #自定义的管理页面
    # url(r'^$', post_list),
    # url(r'^category/(?P<category_id>\d+)/$', post_list),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list),
    # url(r'^post/(?P<post_id>\d+).html', post_detail),
    # url(r'^links/$', links),
    url(r'^$', post_list, name='index'),        #解耦硬编码，url反解
    url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^link/$', links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),
]
