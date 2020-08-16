from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    #re_path(r'^register/$', csrf_exempt(views.viewReg)),
    re_path(r'^login/$', csrf_exempt(views.doLogin)),
    re_path(r'^register/$', csrf_exempt(views.doRegister))
]