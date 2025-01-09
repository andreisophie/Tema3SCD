import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect(host="localhost")
print("Connected to MQTT broker succesfully")
mqttc.loop_start()

for i in range(10):
    mqttc.publish("tema3scd", "Hello, World!")
    print(f"Message sent: Hello, World! {i}")

mqttc.disconnect()
mqttc.loop_stop()