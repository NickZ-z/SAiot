import netaddr
import json 
from django.views.decorators.csrf import csrf_exempt
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




def verify_json():

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
                if (status != 'aberta' and status != 'fechada'):
                    return 'conflited_json'
                else:
                    if is_valid_mac(mac) is False:
                        return 'conflited_mac'
                    else:
                        return {'data':data,'confirmation':True}
        else: 
            print('não foi mandado um json')
            return 'Broken_msg'
    else: 
        print('o tempo acabou na views')
        return 'time_over'
    
@csrf_exempt
def create_device(request):
    if request.method == 'POST':

        data = json.loads(request.body.decode('utf-8'))
        json_string = json.dumps(data)
        print(json_string)
        Publisher.run(json_string)
        json_data_verify = verify_json()
        confirmation_data_verify = str(json_data_verify.get('confirmation'))
        data_verified = json_data_verify.get('data')
        print(type(data_verified))
        print(confirmation_data_verify)
        if confirmation_data_verify:
            
            data_verified = json.dumps(data_verified)
            print(type(data_verified))
            data_verified_str = json.loads(data_verified)
            print(type(data_verified_str))
            mac = data_verified_str.get('mac')
            function_device = data_verified_str.get('funcao')
            status = data_verified_str.get('status')
            print(mac,function_device,status)
            if is_valid_mac(mac) and function_device == 'Porta':
                print('alo')
                device = get_object_or_404(Device,type=function_device)
                print('alo2')
                door_instance = Door.objects.create(mac=mac, status=status, device=device)
                print('alo3')
                door_instance.save()
                print('alo4')
                return JsonResponse({'confirmation': True})
            
            else:
                return JsonResponse({'confirmation': 'conflited_mac'})
            

       
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