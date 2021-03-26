"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import include, path
from pgworker import views
from django.conf.urls import  url
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/',views.upload),
    path('llbug/', include('llbug.urls')),
    path('boardapp/', include('boardapp.urls')),
    path('albumapp/', include('albumapp.urls')),
    path('cartapp/', include('cartapp.urls')),
    path('subiapp/', include('subiapp.urls')),
    path('ch3app/', include('ch3app.urls')),
    path('mdnapp/', include('mdnapp.urls')),
    url(r'^profile/$',TemplateView.as_view(template_name = 'profile.html')),
    url(r'^saveProfile/$', views.saveProfile),
    url(r'^upload_files/$', views.upload_files),
    url(r'^python_board/$', views.board),
    url(r'^view_board/$', views.board),
    url(r'^reptile_board/$', views.board),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^amc_index/$', views.amc_index),
    url(r'^amc_carrer_plan/$', views.amc_carrer_plan),
    url(r'^amc_happy_job/$', views.amc_happy_job),
    url(r'^python_anywhere/$', views.python_anywhere),
    url(r'^git_hub/$', views.git_hub),
    url(r'^django_fw/$', views.django_fw),
    url(r'^bootstrap_fw/$', views.bootstrap_fw),
    url(r'^data_view/$', views.data_view),
    url(r'^data_reptile/$', views.data_reptile),
    url(r'^data_reptile_lessson1/$', views.data_reptile_lessson1),
    url(r'^data_reptile_lessson2/$', views.data_reptile_lessson2),
    url(r'^data_reptile_lessson3/$', views.data_reptile_lessson3),
    url(r'^data_reptile_lessson4/$', views.data_reptile_lessson4),
    url(r'^data_reptile_lessson5/$', views.data_reptile_lessson5),
    url(r'^data_reptile_lessson6/$', views.data_reptile_lessson6),
]
