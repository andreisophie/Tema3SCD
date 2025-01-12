from time import sleep
import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
from re import match
import json
from datetime import datetime

def on_message(client, userdata, message):    
    # Check that topic is valid
    if not match(r"^[^/]+/[^/]+$", message.topic):
        print(f"Invalid topic '{message.topic}', ignoring")
        return
    
    # Print message to stdout
    print(f"Received a message by topic [{message.topic}]")
    
    # Parse message
    split_topic = message.topic.split("/")
    location = split_topic[0]
    station = split_topic[1]
    
    # Parse payload
    parsed_payload = json.loads(message.payload.decode())
    
    # Parse timestamp separately
    if "timestamp" in parsed_payload:
        value = parsed_payload["timestamp"]
        try:
            timestamp = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S%z")
        except ValueError:
            modified_timestamp = value.rsplit(":", 1)[0] + value.rsplit(":", 1)[1]
            timestamp = datetime.strptime(modified_timestamp, "%Y-%m-%dT%H:%M:%S%z")
    else:
        #  If timestamp is not provided, default is now
        timestamp = datetime.now()
    
    data = []
    for key in parsed_payload:
        value = parsed_payload[key]
        # Timestamp was parsed previously
        if key == "timestamp":
            continue
        # Check whether value is a number
        if not isinstance(value, (int, float)):
            continue
        # Create data point
        data.append({
            "measurement": f"{station}.{key}",
            "tags": { "location": location, "station": station },
            "time": timestamp,
            "fields": { "value": value }
        })
        print(f"{location}.{station}.{key} {value}")

    # Write data to InfluxDB
    influxdbc.write_points(data)
    print(f"Written data to InfluxDB")
        
            
print("Starting adapter...")

# Connect to InfluxDB
influxdbc = InfluxDBClient('influxdb', 8086)
databases = influxdbc.get_list_database()
print("Databases: ", databases)
if "tema3scd" not in [db["name"] for db in databases]:
    influxdbc.create_database("tema3scd")
influxdbc.switch_database("tema3scd")

# Connect to MQTT broker
mqttc = mqtt.Client()
mqttc.on_message = on_message

mqttc.connect("mqtt_broker", port=1883)
mqttc.subscribe("#")
mqttc.loop_forever()
