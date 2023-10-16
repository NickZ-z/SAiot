from django.shortcuts import render, redirect,get_object_or_404,HttpResponse

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
    if data != 'Conexão confirmada':
        status = keeper
        return False



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
    