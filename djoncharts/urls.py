# myechartsite/djoncharts/urls.py

from django.conf.urls import url
from . import views

app_name = 'djoncharts'
urlpatterns = [
   url(r'^pyechart3d/$', views.pyechart3d, name='pyechart3d'),
]