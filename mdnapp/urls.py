from django.conf.urls import url
from mdnapp import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^today/$', views.index),
    url(r'^pmv1/$', views.pmv1),
    url(r'^pmv2/$', views.pmv2),
    url(r'^pmv3/$', views.pmv3),
]