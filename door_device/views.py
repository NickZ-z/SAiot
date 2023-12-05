from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import DoorForm, DeviceForm, DeviceFilterForm
from django.core.paginator import Paginator
from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import ipaddress
fail = False

def index(request): 
    devices_on_door = Door.objects.all()

    port_filter = request.GET.get('port_filter', '')
    status_filter = request.GET.get('status_filter', '')
    ip_filter = request.GET.get('ip_filter', '')
    room_filter = request.GET.get('room_filter', '')

    if port_filter:
        devices_on_door = devices_on_door.filter(number_door__icontains=port_filter)
    if status_filter:
        devices_on_door = devices_on_door.filter(status__icontains=status_filter)
    if ip_filter:
      
        devices_on_door = devices_on_door.filter(id__icontains=int(ip_filter))
    if room_filter:

        devices_on_door = devices_on_door.filter(name__exact=room_filter)


    context = {
        'devices': devices_on_door,
    }


    return render(request, 'index.html', context)

def is_valid_ip(ip_str):
    try:
        ipaddress.IPv4Address(ip_str)
        return True
    except ipaddress.AddressValueError:
        try:
            ipaddress.IPv6Address(ip_str)
            return True
        except ipaddress.AddressValueError:
            return False
        
def verify_data():  
    
    Subscriber.run()
    data = Subscriber.get_dataMQTT()
    print(data)
    if data != 'time_over':
        if data != 'fail_json':
            if 'token' not in data or 'ip' not in data or 'funcao' not in data:
                print('json quebrado')
                return False
            else: 
                print('json correto')
                return True
        else: 
            print('não foi mandado um json')
            return False
    else: 
        print('o tempo acabou na views')
        return False
        
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



def verify_device(request):
        Subscriber.run()
        data = Subscriber.get_dataMQTT()
        print(data)
        ip_device = '10.10.101.1'
        function_device = 'Porta'
        print(ip_device)
        if is_valid_ip(ip_device) and function_device == 'Porta':
           
            context = {'funcao':function_device}
           
            return None
        else:
            return JsonResponse({'confirmation': False})

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
    # Obter a instância da porta ou retornar uma resposta 404 se não existir
    device = get_object_or_404(Door, id=device_id)

    # Deletar a instância da porta
    device.delete()

    # Redirecionar para outra página após a exclusão
    return redirect(index)

def edit_door(request, door_id):
    door = get_object_or_404(Door, id=door_id)

    if request.method == 'POST':
        form = DoorForm(request.POST, instance=door)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = DoorForm(instance=door)

    return render(request, 'edit_door.html', {'form': form, 'door': door})