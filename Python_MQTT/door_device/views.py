from django.shortcuts import render, redirect,get_object_or_404
from .forms import DoorForm, DeviceForm
from .models import *

from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *

def index(request): 
    devices_on_door = Door.objects.all()

    return render(request,'index.html',{ 'devices':devices_on_door})

def verify_data(status, keeper):  
    Subscriber.run()
    data = Subscriber.get_dataMQTT()
    print(data)

   
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
    
    return render(request, 'cadastro.html', {'device_form': device_form, 'door_form': door_form})



def send_manssege(request, id):
    
    device = get_object_or_404(Door, id=id)
    
    verify_device = device.status
    if device.status == 'aberta':
        device.status = 'fechada'
        device.save()

        
    elif device.status == 'fechada':
        device.status = 'aberta'
        device.save()
    Publisher.run(device.status)
    
    if verify_data(device.status,verify_device) is False:
        print(device.status)
        return HttpResponse("deu ruim")

    return redirect(index)
    