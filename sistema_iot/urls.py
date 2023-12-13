

from django.contrib import admin
from django.urls import path, include
from door_device.views import *
from door_device.use_cases import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('complete/suap/inicio/', index,name='index'),
    path('sending/<int:id>/', send_manssege, name='msg'),

    path('localizar_IoT/', search_device, name='search_d'),
    path('localizar_IoT/editando/', create_device_edit, name='create_d'),
    path('logout/', logout_index, name='logout'),
    path('sobre_nós/', about_us, name='about_us'),
   
    path('localizar_IoT/delete/', create_device_delete, name='delete_d'),
    path('deletar/<int:device_id>/', deletar_device, name='deletar_device'),
    path('ajuda/', faqs, name='faqs'),
    path('', no_user2, name='no_user'),

    path('confirm/',create_device, name='verify_device'),
    
    path('editando/<int:door_id>/', edit_door, name='edit_door'),

    path('', include('social_django.urls'), name='users'),
]
