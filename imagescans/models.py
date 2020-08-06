from django.db import models


# Create your models here.
class ImageScans(models.Model):
    image = models.FileField(upload_to='ImageScans/', null=True, blank=True)

    def __str__(self):
        return str(self.name)