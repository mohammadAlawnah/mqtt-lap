import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/people_counter"

STUDENT_ID = "12112804" 

client = mqtt.Client(client_id=f"people_pub_{STUDENT_ID}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker (People Counter Publisher)")
    else:
        print("Failed to connect, code =", rc)

client.on_connect = on_connect
client.connect(BROKER, PORT)
client.loop_start()

try:
    counter = 0
    while True:
        change = random.randint(-1, 3)
        counter = max(0, counter + change)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"StudentID={STUDENT_ID}; Type=PEOPLE_COUNT; Value={counter}; Time={timestamp}"

        result = client.publish(TOPIC, message)

        if result[0] == 0:
            print(f"[PUB PEOPLE] Sent -> {message}")
        else:
            print("Failed to send message")

        time.sleep(5)
except KeyboardInterrupt:
    print("Stopping People Counter Publisher...")
finally:
    client.loop_stop()
    client.disconnect()
