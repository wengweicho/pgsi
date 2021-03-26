from django.urls import include
from django.conf.urls import url
from boardapp import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^index/(\w+)/$', views.index),
    url(r'^post/$', views.post),
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^adminmain/$', views.adminmain),
    url(r'^adminmain/(\w+)/$', views.adminmain),
    url(r'^delete/(\d+)/$', views.delete),
    url(r'^delete/(\d+)/(\w+)/$', views.delete),
    url(r'^captcha/', include('captcha.urls')),
]