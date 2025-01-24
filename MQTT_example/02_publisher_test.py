import paho.mqtt.client as mqtt

# MQTT Broker details
BROKER = "14.195.107.2"  # Use a public broker or your own
PORT = 8002                  # Default MQTT port
TOPIC = "test/topic"         # Topic to publish messages to
MESSAGE = "Hello, MQTT!"     # Message to send
QOS = 1                      # Quality of Service level

def on_connect(client, userdata, flags, rc):
    """
    Callback function triggered when the client connects to the broker.
    """
    if rc == 0:
        print("Connected to MQTT broker successfully!")
    else:
        print(f"Connection failed with return code {rc}")

# Create an MQTT client instance
client = mqtt.Client()

# Attach the on_connect callback
client.on_connect = on_connect

# Connect to the MQTT broker
try:
    print(f"Connecting to broker: {BROKER}:{PORT}")
    client.connect(BROKER, PORT, 60)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    exit(1)

# # Publish a message
# try:
#     print(f"Publishing message: {MESSAGE} to topic: {TOPIC}")
#     client.publish(TOPIC, MESSAGE, qos=QOS)
#     print("Message published successfully!")
# except Exception as e:
#     print(f"Failed to publish message: {e}")

# # Disconnect from the broker
# client.disconnect()
