import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/humidity"

STUDENT_ID = "12112804"
client = mqtt.Client(client_id=f"humidity_pub_{STUDENT_ID}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker (Humidity Publisher)")
    else:
        print("Failed to connect, code =", rc)

client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        hum_value = round(random.uniform(40.0, 70.0), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"StudentID={STUDENT_ID}; Type=HUMIDITY; Value={hum_value}; Time={timestamp}"

        result = client.publish(TOPIC, message)
        status = result[0]

        if status == 0:
            print(f"[PUB HUM] Sent -> Topic: {TOPIC} | Message: {message}")
        else:
            print("Failed to send message")

        time.sleep(4)
except KeyboardInterrupt:
    print("Stopping Humidity Publisher...")
finally:
    client.loop_stop()
    client.disconnect()
