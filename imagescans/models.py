from django.db import models
import os
import os


# Create your models here.

class Config():
    UPLOAD_IMAGE_PATH = "/home/akash/projects/django/mriScan/run/media/ImageScans/"
    ANALYZED_IMAGE_PATH = "/home/akash/projects/django/mriScan/run/media/ImageResults/"



class ImageScans(models.Model):
    user_id = models.CharField(max_length=10, )
    image = models.FileField(upload_to='ImageScans' , null=False, blank=False)
    analyzed_image = models.FileField(upload_to='ImageResults', null=True, blank=True)
    
    def save(self):
        for field in self._meta.fields:
            if field.name == 'image':
                field.upload_to = 'ImageScans/%s' % self.user_id
        super(ImageScans, self).save()

    def saveResults(self):
        for field in self._meta.fields:
            if field.name == 'analyzed_image':
                field.upload_to = 'ImageResults/%s' % self.user_id
        super(ImageScans, self).save()


    def __str__(self):
        return str(self.name)
