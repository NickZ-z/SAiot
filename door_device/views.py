from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import *
from door_device.use_cases import * 
from .forms import DoorForm
from django.core.paginator import Paginator
from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import netaddr
import json 

def index(request): 
    devices_on_door = Door.objects.all()
    
    
    return render(request,'index.html',{ 'devices':devices_on_door})

def edit_door(request, door_id):
    door = get_object_or_404(Door, id=door_id)
    
    if request.method == 'POST':
        form = DoorForm(request.POST, instance=door)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index') 
        else:
            print(form.errors)
    else:
        form = DoorForm(instance=door)
    devices2 = Device.objects.all()
    return render(request, 'edit_door.html', {'form': form, 'door': door, 'device':devices2})
        
def send_manssege(request, id):
    global fail
    device = get_object_or_404(Door, id=id)
    
    verify_device = device.status
    if device.status == 'aberta':
        device.status = 'fechada'
        device.save()

        
    elif device.status == 'fechada':
        device.status = 'aberta'
        device.save()
    Publisher.run(device.status)
    
    if verify_data() is False:
        device.status = verify_device
        device.save()
        return JsonResponse({'sua_variavel': True}) and redirect(index)
    
    return JsonResponse({'sua_variavel': False})

def index(request): 
    devices_on_door = Door.objects.all()
    
    return render(request,'index.html',{ 'devices':devices_on_door})


def faqs(request):
    return render(request, 'FAQ.html')

def logout_index(request):
    logout(request)
    return redirect('index')

def login_index(request):
   
    if request.method == 'POST':
        username = request.POST['matricula']
        password = request.POST['senha']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,'login.html')

def about_us(request):
    return render(request, 'about_us.html')



def search_device(request):
   
    return render(request, 'search_device.html')

def cadastro(request):
    device_form = DeviceForm()
    door_form = DoorForm()

    if request.method == 'POST':
        if 'cadastrar_device' in request.POST:
            device_form = DeviceForm(request.POST)
            if device_form.is_valid():
                device_form.save()
        elif 'cadastrar_door' in request.POST:
            door_form = DoorForm(request.POST)
            if door_form.is_valid():
                door_form.save()
    
    return render(request, 'add_device.html', {'device_form': device_form, 'door_form': door_form})
def deletar_device(request, device_id):
    
    device = get_object_or_404(Door, id=device_id)

    
    device.delete()

    # Redirecionar para outra página após a exclusão
    return redirect(index)
