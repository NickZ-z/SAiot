import random

from paho.mqtt import client as mqtt_client


broker = 'www.maqiatto.com'
port = 1883
topic = "nicholas.o@escolar.ifrn.edu.br/T1"
# Generate a Client ID with the publish prefix.
client_id = f'publish-{random.randint(0, 1000)}'
username = 'nicholas.o@escolar.ifrn.edu.br'
password = 'nicholas'

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

def publish(client,msg):
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
    

class Publisher():
    def run(msg):
        client = connect_mqtt()
        client.loop_start()
        publish(client, msg)
        client.loop_stop()

