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
        # Apenas verifica se o MAC é válido, sem verificar se está em uso.
        return True
    except (netaddr.AddrFormatError, ValueError):
        return False
        
def verify_data():  
    
    Subscriber.run()
    data = Subscriber.get_dataMQTT()
    print(data)
    if data != 'time_over':
        if data != 'fail_json':
            if 'token' not in data or 'ip' not in data or 'funcao' not in data or 'status' not in data:
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
def verify_json(data2):
    if data2 != 'time_over':
        if data2 != 'fail_json':
            if 'token' not in data2 or 'ip' not in data2 or 'funcao' not in data2 or 'status' not in data2:
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
    
def create_device(request):
        
        Subscriber.run()
        data = Subscriber.get_dataMQTT()
        

        
        if verify_json(data) is True:
            mac = str(data.get('ip'))
            function_device = str(data.get('funcao'))
            status = str(data.get('status'))
            print(mac, function_device)
        
            if is_valid_mac(mac) and function_device == 'Porta':
                device = get_object_or_404(Device,type=function_device)
                door_instance = Door.objects.create(mac=mac, status=status, device=device)
                door_instance.save()
                return JsonResponse({'confirmation': True})
            else:
                return JsonResponse({'confirmation': False})
        else:
            print('teste')
            return JsonResponse({'confirmation': False})