from time import sleep
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient

def on_message(client, userdata, message):
    # Print message to stdout
    print(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# Connect to InfluxDB
# influxdbc = InfluxDBClient('influxdb', 8086)
# print(influxdbc.get_list_database())

# Connect to MQTT broker
mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.connect("mqtt_broker", port=1883)
mqttc.subscribe("#")
mqttc.loop_forever()
