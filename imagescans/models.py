from django.db import models
import os
# Create your models here.

class Config():
    UPLOAD_IMAGE_PATH = "/home/akash/projects/django/mriScan/run/media/ImageScans/"
class ImageScans(models.Model):
    image = models.FileField(upload_to= 'ImageScans', null=False, blank=False)

    def __str__(self):
        return str(self.name)
    