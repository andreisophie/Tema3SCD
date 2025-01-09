import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

def on_message(client, userdata, message):
    # userdata is the structure we choose to provide, here it's a list()
    userdata.append(message.payload)
    # We only want to process 10 messages
    if len(userdata) >= 10:
        client.unsubscribe("#")

# Connect to InfluxDB
influxdbc = InfluxDBClient('db', 8086)

# Connect to MQTT broker
mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.user_data_set([])
mqttc.connect("mqtt_broker", port=1883)
mqttc.subscribe("#")
mqttc.loop_forever()
print(f"Received the following message: {mqttc.user_data_get()}")