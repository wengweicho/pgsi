from django.conf.urls import url
from cartapp import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^detail/(\d+)/$', views.detail),
    url(r'^addtocart/(\w+)/$', views.addtocart),
    url(r'^addtocart/(\w+)/(\d+)/$', views.addtocart),
    url(r'^cart/$', views.cart),
    url(r'^cartorder/$', views.cartorder),
    url(r'^cartok/$', views.cartok),
    url(r'^cartordercheck/$', views.cartordercheck),
]