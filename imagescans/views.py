from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import ImageScans
from .services import Neuralnetwork
import json
from random import randint


# Create your views here.

def uploadImage(request):
    res = {}
    model = Neuralnetwork()
    try:
        data = request.FILES.get('image')
        rec_n = ImageScans()
        rec_n.image = data
        rec_n.save()
        res['status'] = 1
    except:
        res['status'] = -1
    return JsonResponse(res)
