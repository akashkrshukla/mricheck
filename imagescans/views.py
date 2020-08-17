# Create your views here.
from django.http import JsonResponse
from .models import ImageScans, Config
from .services import Neuralnetwork
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
from random import randint
import os
import numpy as np
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import math

def uploadImage(request):
    res = {}
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id:
            try:
                if os.path.exists(os.path.join(Config.UPLOAD_IMAGE_PATH, (user_id + "/"))):
                    print('Exists')
                else:
                    print('Creating')
                    os.mkdir(os.path.join(Config.UPLOAD_IMAGE_PATH, (user_id + "/")))
                    
            except NotADirectoryError:
                print('Error')
            data = request.FILES.get('image')
            rec_n = ImageScans()
            rec_n.image = data
            rec_n.user_id = user_id
            rec_n.save()
            summary  = evaluateImage(Config.UPLOAD_IMAGE_PATH, user_id)
            rec_n.analyzed_image = data
            rec_n.saveResults()
            res['status'] = 1
            res['summary'] = summary
            return JsonResponse(res)
        else:
            res['status'] = 0
            return JsonResponse(res)


def evaluateImage(base_directory, user_id):
    test_dir = os.path.join(base_directory)

    testAug = ImageDataGenerator(
        rescale=1 / 255.0,
        rotation_range=20,
        zoom_range=0.05,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.05,
        horizontal_flip=True,
        vertical_flip=True,
        fill_mode="nearest")

    testGen = testAug.flow_from_directory(
        test_dir,
        class_mode="categorical",
        target_size=(48, 48),
        color_mode="rgb",
        shuffle=False,
        batch_size=1)

    model = Neuralnetwork.loadModel()
    predIdxs = model.predict(x= testGen)
    predIdxs = np.argmax(predIdxs, axis=1)
    print(testGen.classes, 'test classes')
    print(predIdxs,'predIdxs')
    print(testGen.class_indices.keys(),'testGen.class_indices.keys()')
    # print(classification_report(testGen.classes, predIdxs,
    #                         target_names=testGen.class_indices.keys()))

    # compute the confusion matrix and and use it to derive the raw
    # accuracy, sensitivity, and specificity
    output = {}
    try:
        cm = confusion_matrix(testGen.classes, predIdxs)
        print(cm)
        total = sum(sum(cm))
        acc = (cm[0, 0] + cm[1, 1]) / total
        sensitivity = cm[0, 0] / (cm[0, 0] + cm[0, 1])
        specificity = cm[1, 1] / (cm[1, 0] + cm[1, 1])
        print(acc)
        print(specificity)
        print(sensitivity)
        output['accuracy'] = acc if math.isnan(acc)== False else "NA"
        output['sensitivity'] = sensitivity if math.isnan(sensitivity)== False else "NA"
        output['specificity'] = specificity if math.isnan(specificity)== False else "NA"
    except IndexError:
        print('IndexError')
    output['prediction'] = str(predIdxs[len(predIdxs)-1])
    return output
    # summmary  = model.summary()
    # return summmary
