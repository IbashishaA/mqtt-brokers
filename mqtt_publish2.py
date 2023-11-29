import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# connect client to mqtt_broker
mqttBroker = "localhost"
client = mqtt.Client("Temperature_Outside")
client.connect(mqttBroker, 1883, keepalive=30)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)