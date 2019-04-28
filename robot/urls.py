from django.conf.urls import url
from django.http import JsonResponse,HttpResponse
from . import views
def index(request):
    return JsonResponse({"code":777})
app_name="robot"
urlpatterns = [
    url('^$', index,name="index"),
    # url('robot',views.main)
]
