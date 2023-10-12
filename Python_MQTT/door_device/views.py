from django.shortcuts import render, redirect,get_object_or_404

from .models import *

from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *

def index(request): 
    devices_on_door = Door.objects.all()

    return render(request,'index.html',{ 'devices':devices_on_door})

def verify_data(status, keeper):  
    device = get_object_or_404(Door, id)
    Subscriber.run()
    if Subscriber.timeout_event() == False:
        status = keeper
    data = Subscriber.get_data()
    print(data)

   



def send_manssege(request, id):
    
    print(id)
    device = get_object_or_404(Door, id=id)
    print(str(device))
    verify_device = device.status
    if device.status == 'aberta':
        device.status = 'fechada'
        print(str(device))

        
    elif device.status == 'fechada':
        device.status = 'fechada'
        print(str(device))
      
    
    Publisher.run(str(device))
    Subscriber.run()
    
    return redirect(index)
    