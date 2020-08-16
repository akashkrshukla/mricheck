# Create your views here.
from django.http import JsonResponse
from .models import ImageScans, Config
from .services import Neuralnetwork
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import json
from random import randint
import os


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
            analyzedImage = evaluateImage(Config.UPLOAD_IMAGE_PATH, user_id)
            rec_n.analyzed_image = data
            rec_n.saveResults()
            res['status'] = 1
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
    #return #return analysedImage now.
    # model.predict(x= testGen, steps=(totalTest // 1) + 1)
    # model.summary()  # This can be used to show a detailed summary of model.
