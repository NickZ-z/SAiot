from django.shortcuts import render, redirect,get_object_or_404
from .forms import DoorForm, DeviceForm
from .models import *

from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *

def index(request): 
    devices_on_door = Door.objects.all()

    return render(request,'index.html',{ 'devices':devices_on_door})

def verify_data():  
    Subscriber.run()

    data = Subscriber.get_data()
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
    
    print(id)
    device = get_object_or_404(Door, id=id)
    print(str(device))
    if device.status == 'aberta':
        device.status = 'fechada'
        print(str(device))
        device.save()
    elif device.status == 'fechada':
        device.status = 'aberta'
        print(str(device))
        device.save()
    Publisher.run(str(device))
    verify_data()
    # Redirecione para outra view ou página após a edição
    return redirect(index)  # Redirecione para outra view(request):
    