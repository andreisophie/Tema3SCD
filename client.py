import paho.mqtt.client as mqtt
from time import sleep
import json

mqttc = mqtt.Client()

mqttc.connect(host="localhost", port=1883)
print("Connected to MQTT broker succesfully")
mqttc.loop_start()

topic = "UPB/RPi_1"

payload = {
    "BAT": 99,
    "HUMID" : 40,
    "PRJ" : "SCD",
    "TMP" : 25.3,
    "status": "OK" ,
    "timestamp" : "2024-11-26T03:54:20+03:00"
}

mqttc.publish(topic, payload=json.dumps(payload))
print(f"Published message to topic {topic}")

mqttc.disconnect()
mqttc.loop_stop()