from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    # re_path(r'^register/$', csrf_exempt(views.viewReg)),
    re_path(r'^upload/$', csrf_exempt(views.uploadImage))
]
