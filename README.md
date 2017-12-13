# IdeasX Supervisor 

The purpose of this application is to provide an interface for therapists and care takers to configure and maintain devices in the IdeasX system. The application is cross platform and written in python3.X and PyQt (Qt5). The application currently has the following dependencies: 
    + Python 3.X 
    + PyQt (GUI)
    + Paho-MQTT (Network Communication)
    + PySerial  (Configuration of IdeasX device over USB)

The software only currently supports the IdeasX module v0.3.X, but could be easily modified to support other devices. 

# Paho-MQTT Issue 

The Paho-MQTT mqttc module was modified (in a total hack-ish method). The mqttc does not provde the option to set a timeout for opening a socket. Therefore, if the user enters an incorrect IP / Port, the backend code (wsc_client.py) will hang in-definitly. Therefore, the following line was addded to client.py 
``` 
socket.setDefaultTimeout(1)
```
I'll work on fixing this issue and pushing the update to the Paho repository. 

## List of Brokers 
The following link lists a number of publically available - free - brokers to support IdeasX. 
[https://github.com/mqtt/mqtt.github.io/wiki/public_brokers]
The server I setup using AWS is the following: 
[https://ideasx-cloud.ducksdns.org]
