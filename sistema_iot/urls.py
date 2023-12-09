from django.contrib import admin
from django.urls import path
from door_device.views import *
from faqs.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sending/<int:id>/', send_manssege, name='msg'),
    path('edit_door/<int:door_id>/', edit_door, name='edit_door'),
    path('localizar_IoT/', search_device, name='search_d'),
    path('login/', login_index, name='login'),
    path('logout/', logout_index, name='logout'),
    path('sobre_nós/', about_us, name='about_us'),
    path('categorias/', faq_categorias, name='faq_categorias'),
    path('categoria/<int:categoria_id>/', faq_list, name='faq_list'),
    path('criar_categoria/', criar_categoria, name='criar_categoria'),
    path('enviar_pergunta/<int:categoria_id>/', enviar_pergunta, name='enviar_pergunta'),
    path('enviar_resposta/<int:faq_id>/', enviar_resposta, name='enviar_resposta'),
    path('localizar_IoT/localizar/', faqs, name='localizando'),
    path('deletar/<int:device_id>/', deletar_device, name='deletar_device'),
    path('confirm/', verify_device, name='verify_device'),
    path('', index, name='index'),
]
