from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import ImageScans
import json
from random import randint


# Create your views here.

def uploadImage(request):
    res = {}
    print("hello")
    return JsonResponse(res)
