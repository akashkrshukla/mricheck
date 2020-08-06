from django.contrib import admin
from django.db import models
import django.db.models.deletion

# Register your models here.
from .models import ImageScans


@admin.register(ImageScans)
class ImageScanned(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['name']
