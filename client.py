import paho.mqtt.client as mqtt
from time import sleep

mqttc = mqtt.Client()

mqttc.connect(host="localhost", port=1883)
print("Connected to MQTT broker succesfully")
mqttc.loop_start()

for i in range(10):
    mqttc.publish("tema3scd", "Hello, World!")
    print(f"Message sent: Hello, World! {i}")
    sleep(1)

mqttc.disconnect()
mqttc.loop_stop()