# MQTT Setup

* Connection making and subscription to a topic are two different things.
* Connection can break after subscribing to a topic. Subscription should establish again automatically soon after the reconnection.



+-------------+       Publish       +-------------+
|  Publisher  |  ---------------->  |    Broker    |
+-------------+                     +-------------+
                                       |
                                       | Forward
                                       v
                              +-----------------+
                              |   Subscriber    |
                              +-----------------+


## Install a Broker

```
sudo apt update
sudo apt install mosquitto mosquitto-clients
sudo systemctl start mosquitto
sudo systemctl enable mosquitto
```

verify borker `mosquitto -v` : it starts the mosquitto borker specifically on 1883 port, if mosquitto service is already running then it will create another instance.

**Other Commands**

* `sudo systemctl restart mosquitto` => whenever any modification is done
* `sudo systemctl status mosquitto`


## Configuration file
To allow remote access to your MQTT broker (e.g., Mosquitto), you need to modify its configuration file to define a listener. The listener specifies the network interface and port the broker will use to accept incoming connections, including remote clients.

**File Location**

The default configuration file for Mosquitto is typically located at:
```
/etc/mosquitto/mosquitto.conf (Linux)
/etc/mosquitto/conf.d/ (directory with multiple configuration files)
```

**Step 2: Define the Listener for Remote Access**

To allow remote access, you need to:

1. Define the listener to specify the port.
2. Ensure that the bind address is set to `0.0.0.0` or the `specific IP` address you want to bind to (for remote access).

```
# Enable remote access
listener 1883 0.0.0.0
```

* `1883` is the default MQTT port.
* `0.0.0.0` means the broker will accept connections on all available network interfaces, allowing remote access. If you want to restrict access to specific IP addresses, `replace 0.0.0.0 with a specific IP address (e.g., 192.168.1.100)`.

```
allow_anonymous true
listener 8002 0.0.0.0
```

**Optional: Define SSL/TLS for Encrypted Connections**
If you want to secure the communication, you can also configure `SSL/TLS`:
```
# Enable SSL/TLS for remote connections (optional)
listener 8883
tls_version tlsv1.2
cafile /etc/mosquitto/certs/ca.crt
certfile /etc/mosquitto/certs/server.crt
keyfile /etc/mosquitto/certs/server.key
```

**Optional: Restrict Connections Using Authentication**
If you want to restrict access to your broker to authorized clients, enable authentication and define a password file:

`password_file /etc/mosquitto/passwd`

You can generate the password file using the mosquitto_passwd command:

`sudo mosquitto_passwd -c /etc/mosquitto/passwd my_username`

**Firewall**

If there is any firewall then we need to make sure that traffic is allowed on the port.


**Example of configuration file**

```
# mosquitto.conf

# Default listener (for remote access)
listener 1883 0.0.0.0

# Optional: Enable TLS encryption
# listener 8883
# tls_version tlsv1.2
# cafile /etc/mosquitto/certs/ca.crt
# certfile /etc/mosquitto/certs/server.crt
# keyfile /etc/mosquitto/certs/server.key

# Optional: Enable authentication
password_file /etc/mosquitto/passwd
```




## Subscribe and Publish from Command Line

* to subscribe to single topic: `mosquitto_sub -h localhost -p 8002 -t "home/livingroom/temperature"`
* to Subscribe to all topics under `home/livingroom`: `mosquitto_sub -h localhost -p 8002 -t "home/livingroom/#"` 
* to publish: `mosquitto_pub -h localhost -p 8002 -t "home/livingroom/humidity" -m "45.2"`

## Python Libraries

`pip install paho-mqtt`

### Subscriber example

```
import paho.mqtt.client as mqtt

BROKER = "localhost"  # Change to your broker's IP or hostname
PORT = 1883
TOPIC = "home/livingroom/temperature"

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

```

### Publisher Example

```
import paho.mqtt.client as mqtt
import time

BROKER = "localhost"  # Change to your broker's IP or hostname
PORT = 1883
TOPIC = "home/livingroom/temperature"

def publish():
    client = mqtt.Client()
    client.connect(BROKER, PORT, 60)
    
    try:
        while True:
            temperature = 22.5  # Simulated temperature
            message = f"{temperature}"
            client.publish(TOPIC, message)
            print(f"Published: {message} to topic {TOPIC}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Publisher stopped.")
        client.disconnect()

if __name__ == "__main__":
    publish()

```

### Best Practices

**loop_forever()**
Calling loop_forever() in a Django-based MQTT subscriber connection is not advisable for production use unless it is done in a controlled and isolated manner. 
These are possible issues in `Django` or other large application.

1. Blocks the main thread
    * loop_forever() blocks the execution thread indefinitely, which can prevent Django's request-response cycle or other processes from functioning correctly.
    * Django is designed to handle HTTP requests and responses asynchronously or in a multi-threaded manner. Blocking the thread disrupts this.
2. Scalability Issues: Using loop_forever() in a web server like Gunicorn, uWSGI, or Daphne would lead to problems because it keeps the worker process busy indefinitely, preventing it from serving other requests.

`Recommended Approaches`

1. Use a Separate Background Worker. Run the MQTT subscriber connection in a separate process or thread, independent of the Django web server.
2. Use Django Command for Long-Running Processes: `Run the MQTT subscriber as a custom Django management command.`
3. Use `Asynchronous MQTT Client`: If you are using Django with ASGI (e.g., Django Channels), consider using an asynchronous MQTT library like `gmqtt`.
4. Use a Supervisor or Process Manager: Run the `MQTT subscriber` script as an `independent service` using a process manager like `supervisord or systemd.` This keeps it separate from the Django application but allows for interaction through Django models or APIs.

**should all mqtt subscribers run in different thread in django framework**

Running all MQTT subscribers in separate threads in a Django framework can be a practical approach, but it's not strictly required in all cases. Whether you need separate threads for each subscriber depends on the specific requirements of your application and how you plan to manage connections, subscriptions, and message handling.

`When to Run MQTT Subscribers in Separate Threads`

1. Multiple Topics with Independent Logic: If you have multiple subscribers, each handling different topics with distinct message processing logic, separate threads can help isolate and manage them more effectively.
2. High Concurrency Requirements: If your subscribers need to process a high volume of messages in parallel, separating them into threads (or processes) can improve performance.
3. Avoiding Blocking Operations: To prevent blocking the main thread or other subscribers while processing messages, running each subscriber in its own thread ensures responsiveness.
4. Asynchronous Operations: For operations like database writes or external API calls, separating subscribers into threads or using asynchronous handling avoids bottlenecks.

`Challenges of Multiple Threads`
1. Thread Management Overhead: Creating and managing multiple threads can lead to resource contention, especially if you have many subscribers.
2. Concurrency Issues: Shared resources (e.g., database connections or global variables) must be properly synchronized to avoid race conditions.
3. Scalability Limits: `Python’s Global Interpreter Lock (GIL)` can limit the performance of multi-threaded applications, especially for CPU-bound tasks. For I/O-bound tasks, this is less of an issue.

`Recommended Approaches`
1. Use a Single Thread with Multiple Subscriptions: If your subscribers can share the same connection and there’s no need for heavy processing:
    * Subscribe to multiple topics using a single MQTT client.
    * Handle messages from different topics in a single thread, dispatching them to appropriate handlers.

```
import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print(f"Message received on {message.topic}: {message.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883, 60)
client.subscribe([("topic/1", 0), ("topic/2", 0)])  # Subscribe to multiple topics
client.loop_start()  # Runs in a non-blocking mode
```

2. Use Separate Threads for Each Subscriber: For `distinct logic` per subscriber, run each in its own thread.

```
import threading
import paho.mqtt.client as mqtt

def run_subscriber(topic):
    def on_message(client, userdata, message):
        print(f"Message received on {topic}: {message.payload.decode()}")
    
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("broker.hivemq.com", 1883, 60)
    client.subscribe(topic)
    client.loop_forever()

topics = ["topic/1", "topic/2"]
for topic in topics:
    thread = threading.Thread(target=run_subscriber, args=(topic,))
    thread.start()
```

3. Use Asynchronous Frameworks: For Django applications running with ASGI (e.g., Django Channels), consider using an asynchronous MQTT library like gmqtt to handle multiple subscribers in a non-blocking way.

```
import asyncio
from gmqtt import Client as MQTTClient

class MQTTSubscriber:
    def __init__(self):
        self.client = MQTTClient("django_subscriber")

    async def on_message(self, client, topic, payload, qos, properties):
        print(f"Message received on {topic}: {payload.decode()}")

    async def run(self):
        self.client.on_message = self.on_message
        await self.client.connect("broker.hivemq.com")
        self.client.subscribe("topic/1")
        self.client.subscribe("topic/2")
        await asyncio.Future()  # Keep running

subscriber = MQTTSubscriber()
asyncio.run(subscriber.run())

```

4. Use `Celery` for Message Processing

`Best Practices`
1. Minimize Threads: Avoid creating a separate thread for each subscriber unless necessary. Combine subscriptions where possible.
2. Use Non-blocking Loops: Use loop_start() or async libraries to keep the main thread free.
3. Leverage Message Queues: Forward messages to a message queue (e.g., RabbitMQ, Kafka) for distributed processing.
4. Monitor and Scale: Monitor the resource usage of your subscribers and scale horizontally (e.g., multiple instances) if needed.

**difference between loop_start(), loop_stop() and loop_forever() in mqtt**

Feature	|loop_forever()|	loop_start()	|loop_stop()
---|---|---|---
Blocking	|Yes|	No	|Not applicable (stops the loop)
Thread	|Runs in the current thread|	Runs in a background thread	|Stops the background thread
Use Case|	Simple, standalone MQTT apps|	Concurrent tasks with MQTT|	Stop the background loop
Stopping Needed|	No (blocks indefinitely)|	Yes, using loop_stop()	|N/A

`Best Practices`

1. Use loop_start() for multi-threaded applications where the MQTT client must run in the background without blocking the main thread.
2. Use loop_forever() for simple scripts or testing where MQTT is the sole focus of the program.
3. Always pair loop_start() with loop_stop() to ensure clean shutdown of the background loop.

**Can we use mqtt connect functions multiple times when subscribing to different topics based on demand**

Using the MQTT connect() function multiple times for subscribing to different topics based on demand is not recommended because it creates separate MQTT client connections for each call, which can lead to inefficiency and resource overhead. Instead, it's better to use a single MQTT client connection and dynamically subscribe to or unsubscribe from topics as needed.

`Recommended Approach: Single Connection, Dynamic Subscription`

1. `Single Client Connection`: Create a single MQTT client instance and maintain one connection to the broker.
2. `Dynamic Subscription`: Use the subscribe() method to add new topics and the unsubscribe() method to remove them based on demand.

```
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

def on_message(client, userdata, message):
    print(f"Message received on {message.topic}: {message.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)  # Single connection
client.loop_start()

# Subscribe to topics dynamically
client.subscribe("topic/1")
client.subscribe("topic/2")

# Unsubscribe from topics dynamically
client.unsubscribe("topic/2")

# Keep the program running
import time
time.sleep(10)
client.loop_stop()
client.disconnect()
```

`Handling Demand-Based Subscriptions`

1. For on-demand topic subscriptions: Use a `queue or a signaling mechanism` (e.g., HTTP API, database, or `inter-process communication`) to notify the client about new topics to subscribe to or topics to unsubscribe from.

`When Might Multiple connect() Calls Be Useful?`
1. If you need to connect to different brokers for different sets of topics.
2. If you require isolation between different logical units of your application and cannot achieve it using a single connection.

Even in such cases, minimize the number of connections by grouping related topics under a single connection.

**what will happen if we subscribe separately from connect function and network got disconnected and connected again**

If you subscribe to topics separately from the connect() function and the MQTT client's network connection is lost and reconnected, what happens depends on how your MQTT client and broker are configured.

`Scenario 1: Default Behavior Without Persistent Session`
1. If the network disconnects and reconnects, the MQTT client will not automatically re-subscribe to topics unless you explicitly handle this in your code.
2. The topics you subscribed to after the connect() call will be lost unless they are re-subscribed during or after reconnection.

`Scenario 2: Handling Re-subscription with on_connect`
1. To handle reconnections properly, you can re-subscribe to topics in the on_connect callback. This ensures that whenever the client reconnects, it re-subscribes to all required topics.

```
import paho.mqtt.client as mqtt

# Keep track of topics to subscribe to
TOPICS = [("topic/1", 0), ("topic/2", 0)]

def on_connect(client, userdata, flags, rc):
    print("Reconnected with result code", rc)
    # Re-subscribe to all topics
    for topic, qos in TOPICS:
        client.subscribe(topic, qos)

def on_message(client, userdata, message):
    print(f"Message received on {message.topic}: {message.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

# Subscribe dynamically (but track topics in the global list)
client.subscribe("topic/1", qos=0)
TOPICS.append(("topic/1", 0))  # Add to the tracking list if dynamic

client.loop_forever()
```
Why This Works:
1. The on_connect callback is invoked every time the client connects or reconnects to the broker.
2. Re-subscribing in this callback ensures that your subscriptions are restored after reconnection.

`Scenario 3: Using Persistent Sessions`

If you enable persistent sessions in your MQTT client and broker, subscriptions can survive disconnections without needing re-subscription.

1. How It Works:
    * Set the clean_session flag to False when creating the MQTT client.
    * The broker will remember the client's subscriptions and queue any messages while the client is disconnected.

**does mosquito broker supports persistent sessions**

Yes, the Mosquitto broker supports persistent sessions as defined by the MQTT protocol. Persistent sessions allow the broker to retain a client’s subscription information and queued messages (for QoS 1 and 2) even if the client disconnects.

1. Configuring Mosquitto for Persistent Sessions
2. Using Persistent Sessions in Clients (such as paho library): set `clean_session or clean_start` to `False`



## Clients limit for MQTT
The number of MQTT subscriber clients that can run on a single Ubuntu server depends on several factors, including the server's hardware resources, the MQTT broker being used, and the nature of the MQTT communication (e.g., message frequency, payload size, QoS levels).

**Operating System and Configuration:**

Apart from several other factors, it is very important as well. Linux, including Ubuntu, can handle many open connections, but the default limit for file descriptors (open sockets) is often low (e.g., 1024). This can be increased by adjusting system settings.

1. `Increase File Descriptor Limit`: Each MQTT connection uses a file descriptor. Increase the limit by editing /etc/security/limits.conf:

    * soft nofile 100000
    * hard nofile 100000
Also, configure `ulimit` and adjust `systemd` service limits if needed.

`NOTE: Client and Subscriber are different things. A client can have multiple subscribers`


## Separate Clients for Subscriber and Publisher
Yes, creating separate MQTT clients for subscribers and publishers can be a good practice depending on your use case and system requirements. While a single MQTT client can handle both subscribing and publishing, separating the two roles has several advantages. 

Advantages of Separate MQTT Clients
Separation of Concerns:

Each client can focus on a single responsibility: publishing or subscribing, simplifying the logic in your application.
Scalability:

You can independently scale publishers and subscribers based on their workloads.
For example, a system might need many subscribers for data processing but fewer publishers.
Reliability:

If one client encounters issues (e.g., the subscriber), it won’t affect the other (e.g., the publisher), increasing overall system robustness.
Performance:

Separate clients reduce the likelihood of resource contention, such as message processing delays when handling both publishing and subscribing.
Security:

With separate clients, you can assign different access permissions for each role in the broker's ACL (Access Control List).
For example:
Publisher client: Write-only permission on a specific topic.
Subscriber client: Read-only permission on that topic.
Protocol or Library Limitations:

Some MQTT libraries or implementations may have constraints when handling both roles in a single client, making separate clients a better choice.

### Best Practices

1. Unique Client IDs: Ensure each client has a unique identifier to avoid conflicts.
2. Topic Wildcards: Use MQTT `wildcards (e.g., + or #)` for subscribers if `multiple topics` are involved.
3. Resource Management: Monitor and optimize memory and CPU usage, especially on constrained devices.
4. Broker Configuration: Define separate roles and permissions for publishers and subscribers in the broker's configuration.

**what happens to the messages in publishers keeps publishing the data but there is no subscriber**

If an MQTT publisher keeps publishing data to a topic that has no subscribers, the behavior depends on the following factors: QoS level, retained messages, and the configuration of the MQTT broker. Here's a breakdown:

1. No Subscriber, QoS Level Behavior
QoS 0 ("At most once"):

The message is sent to the broker without any guarantee of delivery.
If no subscriber is present at the time of publishing, the broker discards the message immediately.
QoS 1 ("At least once"):

The broker acknowledges the receipt of the message from the publisher.
If there are no subscribers, the broker holds the message briefly to attempt delivery but ultimately discards it since there's no target client.
QoS 2 ("Exactly once"):

The broker ensures the message is received exactly once by any subscriber.
If no subscriber exists, the broker completes the acknowledgment process with the publisher but discards the message afterward.
In all cases, if there are no subscribers, the message does not persist unless a retained message is used.

2. Retained Messages
If the message is published as a retained message, the broker stores the message and associates it with the topic.
When a new subscriber subscribes to the topic, the broker immediately sends the last retained message to the subscriber.
Example:
python
Copy
Edit
publisher.publish("sensor/data", "Temperature: 22°C", retain=True)
3. Broker-Level Behavior
By default, most MQTT brokers discard messages for topics with no subscribers.
Some brokers may provide configurations to buffer messages for future subscribers, but this is not standard behavior and can lead to resource issues if used extensively.
4. Implications in a Real-World Scenario
Data Loss:
Messages published to topics with no subscribers are typically discarded unless retained.
Wasted Resources:
Network and processing resources are used to transmit and process messages that are discarded.
System Design:
Systems that require message persistence for future subscribers must use retained messages or integrate message storage mechanisms (e.g., database, message queue).
5. Best Practices
Use Retained Messages:

For topics where you want subscribers to receive the latest message upon connecting.
Monitor Subscriptions:

Track active subscribers using broker tools or APIs (e.g., Mosquitto or EMQX provides ways to view active clients).
Buffering Mechanisms:

If you need to store messages for offline subscribers, consider integrating with a message queue system (e.g., Kafka, RabbitMQ) or enabling persistence in the broker (if supported).
Publish Only When Necessary:

Ensure publishers only send data when at least one subscriber exists, if applicable, to reduce resource usage.
Summary
If a publisher sends messages to a topic with no subscribers:
Without retained messages, the broker discards the messages.
With retained messages, the broker stores the last message for future subscribers.
QoS levels determine delivery guarantees but do not affect message retention unless a subscriber is present.
Implementing retained messages or buffering mechanisms can ensure critical data is available to future subscribers.


## Architecture

**should MQTT operation handling application be separate than the main django code**

Whether an MQTT operation-handling application should be separate from the main Django code depends on the architectural needs, complexity, and performance requirements of your project. Below, I outline the considerations for keeping it separate versus integrating it into the Django code.

1. Integrating MQTT with Django
Advantages:
Simplicity:

Easier to manage since all application logic resides in one place.
Useful for small to medium-sized projects where MQTT operations are straightforward.
Shared Resources:

Direct access to Django’s ORM, models, and configurations.
No need for inter-process communication between the MQTT handler and Django app.
Reduced Deployment Overhead:

Fewer services to deploy, monitor, and maintain.
Disadvantages:
Scalability Issues:

Handling MQTT operations (e.g., subscribing to topics, processing messages) may consume resources and impact the performance of the web application.
Complexity in Concurrency:

MQTT relies on an event-driven model and is often asynchronous, while Django is typically synchronous (unless using ASGI).
Mixing these paradigms can complicate the codebase.
Potential Blocking:

Long-running MQTT message-handling operations can block Django’s request-handling threads, degrading API responsiveness.
2. Keeping MQTT Operations Separate from Django
Advantages:
Improved Performance and Scalability:

The MQTT handler runs independently, ensuring it doesn’t impact Django’s web request handling.
Each component can be scaled independently based on its workload.
Decoupling:

Separating concerns allows for cleaner code and independent development cycles.
Makes it easier to use different technologies optimized for MQTT (e.g., asyncio, Node.js).
Fault Isolation:

Issues in the MQTT handler won’t crash or slow down the Django application.
Asynchronous Processing:

The MQTT handler can use libraries like paho-mqtt or frameworks optimized for event-driven tasks (e.g., Celery with Redis or RabbitMQ).
Disadvantages:
Additional Infrastructure:

Requires inter-process communication (e.g., via a database, message broker, or REST APIs) between Django and the MQTT handler.
Deployment Complexity:

More services to deploy and manage.
3. Use Case-Based Recommendation
When to Integrate MQTT with Django:
Small-scale applications where MQTT message volumes are low.
Scenarios where MQTT logic is simple and does not involve long-running tasks.
You want to prototype or deploy quickly with minimal overhead.
When to Separate MQTT from Django:
High-volume MQTT message processing.
Scenarios requiring scalability or fault tolerance for MQTT operations.
Use cases involving heavy asynchronous processing or external system integrations.
Large-scale systems with a microservices architecture.
4. Architecture for a Separate MQTT Handler
Run an Independent MQTT Handler:

Use a standalone script or service (e.g., Python with paho-mqtt or Node.js with mqtt.js).
Example:
python
Copy
Edit
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()}")
    # Process and send data to Django (e.g., via an API or database)

client = mqtt.Client()
client.on_message = on_message
client.connect("broker.hivemq.com", 1883)
client.subscribe("sensor/data")
client.loop_forever()
Use a Shared Data Store:

Save MQTT messages to a shared database, message queue (e.g., Redis, RabbitMQ), or Django’s models.
Communicate via REST or WebSocket APIs:

Let the MQTT handler call Django APIs to save or retrieve data.
5. Example Deployment Options
Integrated Deployment:

Use Django with an ASGI server (e.g., Daphne or Uvicorn) to handle both HTTP and MQTT asynchronously.
Separate Deployment:

Deploy Django for HTTP requests and a separate service (e.g., Python script, Node.js app) for MQTT.
Use a message broker (e.g., Redis or Kafka) for inter-process communication if needed.
6. Conclusion
Small Applications: Integrate MQTT into Django for simplicity.
Scalable or Complex Systems: Use a separate MQTT handler for better performance, scalability, and fault isolation.
The decision should align with your system’s complexity, traffic patterns, and future scalability requirements.


## Keep Alive
The `keep-alive` setting in `Mosquitto MQTT broker` defines how often a client must send a message (PINGREQ or actual data) to maintain the connection. This prevents the broker from assuming the client is offline.

**How Does Keep-Alive Work?**

* When a client connects to the broker, it specifies a keep-alive interval (in seconds).
* If the broker does not receive any message from the client within 1.5 times the keep-alive interval, it disconnects the client.
* The client sends PINGREQ messages periodically if no data is being transmitted, and the broker responds with PINGRESP.

✅ Setting Keep-Alive in Mosquitto
1️⃣ Configure Keep-Alive in Client (Recommended)
Clients can set the keep-alive interval when connecting.

🔸 In Arduino (Using ArduinoMqttClient Library)
```
mqttClient.setKeepAliveInterval(30);  // Set keep-alive to 30 seconds
mqttClient.connect(mqtt_server, mqtt_port);
```
✔️ Ensures the broker expects a message every 30 seconds.

2️⃣ Configure Keep-Alive in Mosquitto Broker
You can set default keep-alive behavior in Mosquitto’s configuration file.

`Edit the Mosquitto Config File (e.g., /etc/mosquitto/mosquitto.conf):`
```
keepalive_interval 60
```
Restart Mosquitto:
sh
Copy
Edit
```
sudo systemctl restart mosquitto
```
✔️ This sets the default keep-alive for clients not explicitly setting it.

🔹 What Happens If Keep-Alive Fails?
If a client misses its keep-alive deadline:

The broker disconnects the client.
If LWT (Last Will and Testament) is set, the broker sends an offline status message.

🔹 Default Keep-Alive Interval in Mosquitto
The default keep-alive interval in the Mosquitto MQTT broker depends on the client settings:

If the client specifies a keep-alive interval, Mosquitto uses that value.
If the client does not specify a keep-alive interval, Mosquitto defaults to 60 seconds.

🔹 What Happens If a Client Exceeds Keep-Alive?
If a client fails to send a message (publish, subscribe, or PINGREQ) within 1.5 times the keep-alive interval, the broker disconnects the client.
Example:
Keep-alive = 60 sec
Mosquitto waits up to 90 sec (1.5 × 60 sec) before disconnecting the client.


🔹 Default Keep-Alive Interval in Mosquitto
The default keep-alive interval in the Mosquitto MQTT broker depends on the client settings:

If the client specifies a keep-alive interval, Mosquitto uses that value.
If the client does not specify a keep-alive interval, Mosquitto defaults to 60 seconds.
🔹 What Happens If a Client Exceeds Keep-Alive?
If a client fails to send a message (publish, subscribe, or PINGREQ) within 1.5 times the keep-alive interval, the broker disconnects the client.
Example:
Keep-alive = 60 sec
Mosquitto waits up to 90 sec (1.5 × 60 sec) before disconnecting the client.
🔹 How to Change the Keep-Alive Interval?
1️⃣ On the Client Side (Recommended)
Set the keep-alive interval when connecting:

In Arduino (Using ArduinoMqttClient Library):
cpp
Copy
Edit
mqttClient.setKeepAliveInterval(30);  // Set keep-alive to 30 seconds
In Python (Using paho-mqtt Library):
python
Copy
Edit
client.connect("broker.hivemq.com", 1883, keepalive=45)  # 45 sec
In Mosquitto CLI (mosquitto_sub or mosquitto_pub):
sh
Copy
Edit
mosquitto_sub -h broker.hivemq.com -t "test/topic" -k 30
2️⃣ On the Mosquitto Broker Side
If you want Mosquitto to enforce a default keep-alive interval, you can modify its configuration:

Edit the Mosquitto config file (/etc/mosquitto/mosquitto.conf):
ini
Copy
Edit
keepalive_interval 120  # Set default keep-alive to 120 seconds
Restart Mosquitto for changes to take effect:
sh
Copy
Edit
sudo systemctl restart mosquitto

