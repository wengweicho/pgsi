from django.conf.urls import url
from subiapp import views

urlpatterns = [
    url(r'^$', views.taiwan_map),
    url(r'^taiwan_map/$', views.taiwan_map),
    url(r'^subiinfo_uploadfile/$', views.subiinfo_uploadfile),
    url(r'^taiwan_map/(..[市縣修刪])/$', views.taiwan_map),
    url(r'^admissions/$', views.admissions),
    url(r'^trust/$', views.trust),
    url(r'^delete_onerecord/(\S\S)/$', views.delete_onerecord),
    url(r'^modify_onerecord/(\S\S)/$', views.modify_onerecord),
    url(r'^login/$', views.login),
    url(r'^login/(\S\S)/$', views.login),
]

