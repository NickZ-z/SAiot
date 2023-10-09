import random

from paho.mqtt import client as mqtt_client


broker = 'www.maqiatto.com'
port = 1883
topic = "nicholas.o@escolar.ifrn.edu.br/T1"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'nicholas.o@escolar.ifrn.edu.br'
password = 'nicholas'
data = None

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global data
        data = msg.payload.decode() 
        print(data)
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
       
        client.disconnect()
        print("desconectado")
    client.subscribe(topic)
    client.on_message = on_message

class Subscriber():
    def get_data():
        global data
        return data
    
    def run():
        client = connect_mqtt()
        subscribe(client)
        
        client.loop_forever()
       