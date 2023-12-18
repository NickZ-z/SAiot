import netaddr
import json 
from .models import *
from django.shortcuts import render, redirect,get_object_or_404,HttpResponse
from django.http import JsonResponse
from mqtt_protocol.publisher import *
from mqtt_protocol.subscribe import *

def is_valid_mac(mac_str):
    try:
        mac = netaddr.EUI(mac_str)
        
        return True
    except (netaddr.AddrFormatError, ValueError):
        return False
        
def verify_data(previous_status,mac_models):  
    
    Subscriber.run()
    data = Subscriber.get_dataMQTT()

   
    if data != 'time_over':
        if data != 'fail_json':
            if 'token' not in data or 'mac' not in data or 'funcao' not in data or 'status' not in data:
                print('json quebrado')
                return 'JSON_invalid'
            else: 
                status = data.get('status')
                mac = data.get('mac')
                if status == previous_status or (status != 'aberta' and status != 'fechada'):
                    return 'conflited_json'
                else:
                    if mac != mac_models:
                        return 'conflited_mac'
                    else:
                        return True
                
        else: 
            print('não foi mandado um json')
            return 'Broken_msg'
    else: 
        print('o tempo acabou na views')
        return 'time_over'




def verify_json(data):
    if data != 'time_over':
        if data != 'fail_json':
            if 'token' not in data or 'mac' not in data or 'funcao' not in data or 'status' not in data:
                print('json quebrado')
                return 'JSON_invalid'
            else: 
                print('json correto')
                return True
        else: 
            print('não foi mandado um json')
            return 'Broken_msg'
    else: 
        print('o tempo acabou na views')
        return 'time_over'
    
def create_device(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        

        return JsonResponse({'confirmation': True})
        #if verify_json(data) == True:
        #   mac = str(data.get('mac'))
        #    function_device = str(data.get('funcao'))
        #   status = str(data.get('status'))
        #    print(mac, function_device)
        
         #   if is_valid_mac(mac) and function_device == 'Porta':
          #      device = get_object_or_404(Device,type=function_device)
           #     door_instance = Door.objects.create(mac=mac, status=status, device=device)
            #    door_instance.save()
                
            #else:
             #   return JsonResponse({'confirmation': 'conflited_mac'})
       # else:
        #    vd = verify_json(data)
         #   return JsonResponse({'confirmation': vd})
        
    else:
        print('deu ruim')
        return JsonResponse({'confirmation': False})