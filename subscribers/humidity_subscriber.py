import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/humidity"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker (Humidity Subscriber)")
        client.subscribe(TOPIC)
        print("Subscribed to:", TOPIC)
    else:
        print("Failed to connect, code =", rc)

def on_message(client, userdata, msg):
    message = msg.payload.decode()
    print(f"[SUB HUM] Received: {message}")

client = mqtt.Client(client_id="humidity_subscriber")
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)
client.loop_forever()
