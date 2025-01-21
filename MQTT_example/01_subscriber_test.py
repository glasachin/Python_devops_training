import paho.mqtt.client as mqtt

BROKER = "14.195.107.2"  # Change to your broker's IP or hostname
PORT = 8002
TOPIC = "daq/test"

def on_connect(client, userdata, flags, rc):
    print(f"Connected to broker with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} from topic {msg.topic}")

def subscribe():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect(BROKER, PORT, 60)
    client.loop_forever()

if __name__ == "__main__":
    subscribe()