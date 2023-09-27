from django.contrib import admin
from .models import *

@admin.register(Doors)
class DoorsAdmin(admin.ModelAdmin):
    list_display = ("type",)

@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ("ip","number_door","status","door",)