"""MySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import xadmin

from django.conf.urls.static import static,serve
from django.conf.urls import url, include
from django.views import static

from . import settings

urlpatterns = [
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'ueditor/', include('DjangoUeditor.urls')),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'', include('comments.urls', namespace='comments')),
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]


#定义404和500页面
handler404 = "blog.views.page_not_found"
handler500 = "blog.views.page_error"
