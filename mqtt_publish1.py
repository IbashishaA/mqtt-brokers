import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

# connect client to mqtt_broker
mqttBroker = "localhost"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker, 1883, keepalive=30)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to Topic TEMPERATURE")
    time.sleep(1)