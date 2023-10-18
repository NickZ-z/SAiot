

from django.contrib import admin
from django.urls import path
from door_device.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('teste/<int:id>/', send_manssege, name='msg'),
    path('cadastro/', cadastro, name='cadastro'),
   
]
