from django.contrib import admin
from .models import *

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("type",)

@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):
    list_display = ("name","ip","number_door","status","device",)