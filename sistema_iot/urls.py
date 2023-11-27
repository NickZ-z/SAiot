

from django.contrib import admin
from django.urls import path, include
from door_device.views import *

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='index'),
    path('teste/<int:id>/', send_manssege, name='msg'),
    path('localizar_IoT/cadastro/', cadastro, name='cadastro'),
    path('localizar_IoT/', search_device, name='search_d'),
    path('login/', login_index, name='login'),
    path('logout/', logout_index, name='logout'),
    path('sobre_nós/', about_us, name='about_us'),
    path('FAQs/', faqs, name='faqs'),
    path('localizar_IoT/localizar/', faqs, name='localizando'),
    path('deletar/<int:device_id>/', deletar_device, name='deletar_device'),
     
    path('confirm/',verify_device, name='verify_device'),
    
    path('', include('social_django.urls'), name='social'),
]
