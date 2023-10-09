from django.shortcuts import render, redirect,get_object_or_404

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
    