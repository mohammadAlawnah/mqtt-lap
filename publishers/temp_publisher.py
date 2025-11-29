import time
import random
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "lab/temperature"

STUDENT_ID = "12112804" 

client = mqtt.Client(client_id=f"temp_pub_{STUDENT_ID}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker (Temperature Publisher)")
    else:
        print("Failed to connect, code =", rc)

client.on_connect = on_connect

client.connect(BROKER, PORT)
client.loop_start()

try:
    while True:
        temp_value = round(random.uniform(20.0, 30.0), 2)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"StudentID={STUDENT_ID}; Type=TEMPERATURE; Value={temp_value}; Time={timestamp}"

        result = client.publish(TOPIC, message)
        status = result[0]

        if status == 0:
            print(f"[PUB TEMP] Sent -> Topic: {TOPIC} | Message: {message}")
        else:
            print("Failed to send message")

        time.sleep(3)
except KeyboardInterrupt:
    print("Stopping Temperature Publisher...")
finally:
    client.loop_stop()
    client.disconnect()