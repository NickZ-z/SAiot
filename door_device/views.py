from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import *
from .forms import DoorForm, DeviceForm
from django.core.paginator import Paginator
from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import ipaddress
fail = False

def index(request): 
    devices_on_door = Door.objects.all()
    
    paginator = Paginator(devices_on_door, 3)
    pagina = request.GET.get('page')
    itens = paginator.get_page(pagina)
    return render(request,'index.html',{ 'devices':itens, 'fail': fail})

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
    
    if data != 'Conexão confirmada':
        
        return False
def verify_device(request):
        Subscriber.run()
        data = Subscriber.get_dataMQTT()
        print(data)
        ip_device = data.get('ip')
        function_device = data.get('funcao')
        
        print(ip_device)
        if is_valid_ip(ip_device) and function_device == 'porta':
            device = Device.objects.get(type='Porta')
            new_device = Door(ip=ip_device, device=device)
            new_device.save()
            resposta = {'confirmation': True}

            return JsonResponse(resposta)
        else:
            return JsonResponse({'confirmation': False})

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
        fail == True
        return redirect(index)
    fail == False
    return redirect(index)

def index(request): 
    devices_on_door = Door.objects.all()
    paginator = Paginator(devices_on_door, 3)
    pagina = request.GET.get('page')
    itens = paginator.get_page(pagina)
    return render(request,'index.html',{ 'devices':itens})


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
    
    return render(request, 'search_device.html', {})

   
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