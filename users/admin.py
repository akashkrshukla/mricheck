from django.contrib import admin
from .models import user

# Register your models here.

@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    actions_on_top = True
    actions_on_bottom = True
    search_fields = ['name']

