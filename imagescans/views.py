from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import ImageScans, Config
from .services import Neuralnetwork
import json
from random import randint
from sklearn.metrics import classification_report
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import LearningRateScheduler
from tensorflow.keras.optimizers import Adagrad
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

###################
# library dependencies
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os


# Create your views here.

def uploadImage(request):
    res = {}
    data = request.FILES.get('image')
    rec_n = ImageScans()
    rec_n.image = data
    rec_n.save()
    evaluateImage(Config.UPLOAD_IMAGE_PATH)
    res['status'] = 1
    # try:
    #     data = request.FILES.get('image')
    #     rec_n = ImageScans()
    #     rec_n.image = data
    #     rec_n.save()
    #     evaluateImage(rec_n.image)
    #     res['status'] = 1
    # except:
    #     res['status'] = -1
    return JsonResponse(res)


def evaluateImage(image):
    model = Neuralnetwork.loadModel()
    # model.summary()  # This can be used to show a detailed summary of model.
