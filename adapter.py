from time import sleep
import paho.mqtt.client as mqtt
import logging
from influxdb import InfluxDBClient

def on_message(client, userdata, message):
    # Print message to stdout
    logging.info(f"Received message '{message.payload.decode()}' on topic '{message.topic}'")

# Connect to InfluxDB
influxdbc = InfluxDBClient('influxdb', 8086)
logging.info(influxdbc.get_list_database())

def main():
    logging.info("Starting adapter...")
    # Connect to MQTT broker
    mqttc = mqtt.Client()
    mqttc.on_message = on_message

    mqttc.connect("mqtt_broker", port=1883)
    mqttc.subscribe("#")
    mqttc.loop_start()

    while True:
        logging.info("I am alive! Waiting for messages...")
        sleep(5)

if __name__ == "__main__":
    main()