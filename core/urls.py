
from django.conf.urls import url
from . import views

from django.http import HttpResponse,JsonResponse

def index(request):
    return JsonResponse({"code":1888})

app_name = 'core_templates'
urlpatterns = [
    url(r'^$',index,name="index"),
   url(r'vivo', views.vivo, name='vivo'),
   url(r'rr', views.rr, name='rr'),
   url(r'datatable', views.data_table),
   url(r'Check', views.Check),
   url(r'add', views.add),
   url(r'index', views.index),
]