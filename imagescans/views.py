# Create your views here.
from django.http import JsonResponse
from .models import ImageScans, Config
from .services import Neuralnetwork


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
    model = Neuralnetwork()
    model.summary()
    # model.summary()  # This can be used to show a detailed summary of model.
