# MQTT Lab – Mosquitto Broker + Paho Clients

**Student ID:** 12112804  

This project demonstrates a full MQTT setup using:
- Mosquitto MQTT Broker
- Mosquitto MQTT Broker
- Three sensors (Temperature, Humidity, People Counter)
- Each message contains the student ID as required.

---

##  How the MQTT System Works

This lab demonstrates a complete MQTT workflow using **Mosquitto Broker** and **Paho-MQTT Python clients**.

### The workflow:

1. **Mosquitto Broker**  
   - Acts as the central message router.  
   - Runs locally on port **1883**.  
   - Publishers send messages to the broker.  
   - Subscribers receive messages from the broker based on topics.

2. **Sensors (Publishers)**  
   Three simulated sensors send data every few seconds:
   - Temperature Sensor → publishes to `lab/temperature`
   - Humidity Sensor → publishes to `lab/humidity`
   - People Counter Sensor → publishes to `lab/people_counter`

   Each published message includes:
   - Student ID (12112804)  
   - Sensor Type  
   - Random Value  
   - Timestamp  

3. **Subscribers**  
   A subscriber listens to a specific topic and prints all incoming messages in real time.

4. **Communication Flow Example**
Publisher → sends → Mosquitto Broker → delivers → Subscriber


5. **All components were tested together with screenshots included below.**
