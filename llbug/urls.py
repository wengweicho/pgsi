from django.conf.urls import url
from llbug import views

urlpatterns = [
    url(r'^$', views.index),

]
