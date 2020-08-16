from tensorflow import keras
from django.db import models


class Neuralnetwork(models.Model):
    def __init__(self):
        model = keras.models.load_model('optimised_model.hdf5')

    @staticmethod
    def loadModel():
        print("\n\nloading saved model")
        model = keras.models.load_model('my_model')
        #model = keras.models.load_model('optimised_model.hdf5')
        return model
