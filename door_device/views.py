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
from django.contrib.auth.decorators import login_required
def index(request): 
    devices_on_door = Door.objects.all()
    
    port_filter = request.GET.get('port_filter', '')
    status_filter = request.GET.get('status_filter', '')
    ip_filter = request.GET.get('ip_filter', '')
    room_filter = request.GET.get('room_filter', '')
    print(ip_filter)
    if port_filter:
        devices_on_door = devices_on_door.filter(number_door__icontains=port_filter)
    if status_filter:
        devices_on_door = devices_on_door.filter(status__icontains=status_filter)
    if ip_filter:
      
        devices_on_door = devices_on_door.filter(mac__icontains=str(ip_filter))
    if room_filter:

        devices_on_door = devices_on_door.filter(name__exact=room_filter)

    return render(request,'index.html',{ 'devices':devices_on_door})
def create_device_delete(request):
    
    device = Door.objects.last()

    
    device.delete()

    
    return redirect(index)
def create_device_edit(request): 
    door = Door.objects.last()
    
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
    return render(request, 'edit_door.html', { 'form': form,'door': door, 'device':devices2})
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
   
    device = get_object_or_404(Door, id=id)
    
    previous_status = device.status
    if device.status == 'aberta':
        device.status = 'fechada'
        device.save()

        
    elif device.status == 'fechada':
        device.status = 'aberta'
        device.save()
    Publisher.run(device.status)
    vd = verify_data(previous_status,device.mac)
    print(vd)
    if vd is True:
        
        return JsonResponse({'sua_variavel': True}) 
    else:
        device.status = previous_status
        device.save()
        print(vd)
        return JsonResponse({'sua_variavel': vd})




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

def no_user2(request):
    if request.user.is_authenticated:
        return redirect('index') 
    return render(request,'no_user.html')

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
