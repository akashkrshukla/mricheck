from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import ImageScans, Config
from .services import Neuralnetwork
import json
from random import randint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report


###################
#library dependencies
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

NUM_EPOCHS = 2 #40
INIT_LR = 1e-2
BS = 32

# Create your views here.

def uploadImage(request):
    res = {}
    data = request.FILES.get('image')
    rec_n = ImageScans()
    rec_n.image = data
    rec_n.save()
    print(rec_n.image)
    print(type(rec_n.image))
    evaluateImage(Config.UPLOAD_IMAGE_PATH)
    #evaluateImage(request.FILES.get(rec_n.image))
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

def preProcessImage():
    print("processing image")

def createAndBuildModel():
    model = Neuralnetwork.build(width=48, height=48, depth=3,
	classes=2)
    H = model.fit(
	x=trainGen,
	steps_per_epoch=totalTrain // BS,
	validation_data=valGen,
	validation_steps=totalVal // BS,
	class_weight=classWeight,
	epochs=NUM_EPOCHS)
    return model

def evaluateImage(image):
    # determine the total number of image paths in training, validation,
    # and testing directories
    # trainPaths = list(paths.list_images(config.TRAIN_PATH))
    # totalTrain = len(trainPaths)
    # totalVal = len(list(paths.list_images(config.VAL_PATH)))
    totalTest = len(list(paths.list_images(Config.UPLOAD_IMAGE_PATH)))
    model = Neuralnetwork.build(width=48, height=48, depth=3,
	classes=2)
    valAug = ImageDataGenerator(rescale=1 / 255.0)
    # initialize the testing generator
    testGen = valAug.flow_from_directory(
        image,
        class_mode="categorical",
        target_size=(48, 48),
        color_mode="rgb",
        shuffle=False,
        batch_size=BS)

    # reset the testing generator and then use our trained model to
    # make predictions on the data
    print("[INFO] evaluating network...")
    testGen.reset()
    predIdxs = model.predict(x=testGen, steps=(totalTest // BS) + 1)

    # for each image in the testing set we need to find the index of the
    # label with corresponding largest predicted probability
    predIdxs = np.argmax(predIdxs, axis=1)

    # show a nicely formatted classification report
    print(classification_report(testGen.classes, predIdxs,
        target_names=testGen.class_indices.keys()))

