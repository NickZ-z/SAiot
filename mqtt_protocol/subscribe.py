import random
import threading
from paho.mqtt import client as mqtt_client
import json

broker = 'www.maqiatto.com'
port = 1883
topic = "nicholas.o@escolar.ifrn.edu.br/T1"
client_id = f'publish-{random.randint(0, 1000)}'
username = 'nicholas.o@escolar.ifrn.edu.br'
password = 'nicholas'

data = None
timeout_seconds = 20
stop_search = False
timeout_thread = 0
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
            
        
    def on_disconnect(client, userdata, rc):
        if rc != 0:
            print(f"Desconectado inesperadamente, código de retorno: {rc}")
        else:
            print("Desconexão bem-sucedida")
        global stop_search
        timeout_thread.cancel()
        stop_search = True
        print("time cancel")
            
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    
    
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.connect(broker, port)
    return client
    
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global data
        
        data = msg.payload.decode() 
        
        print("Mensagem recebida:", data)
    
        client.disconnect()
        
        
        
    client.subscribe(topic)
    client.on_message = on_message
    

class Subscriber():
    def statusTimer(status):
        if status == True:
            return True
        else:
            return False
    def get_dataMQTT():
        global data
        return data
    def timeout_event():
        global stop_search
        print("Acabou o tempo")
        stop_search = True
    def run():
        client = connect_mqtt()
        subscribe(client)
        global stop_search
        stop_search = False
        global timeout_thread
        timeout_thread = threading.Timer(timeout_seconds, Subscriber.timeout_event)
        timeout_thread.start()
        while stop_search == False:
            client.loop()
       