from django.db import models


# Create your models here.

class user(models.Model):
    user_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=70, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    age = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=60)
    
    def __str__(self):
        return str(self.name) + '-' + str(self.mobile)


