<<<<<<< HEAD
# IdeasX Supervisor 

The purpose of this application is to provide an interface for therapists and care takers to configure and maintain devices in the IdeasX system. The application is cross platform and written in python3.X and PyQt (Qt5). The application currently has the following dependencies: 
    + Python 3.X 
    + PyQt (GUI)
    + Paho-MQTT (Network Communication)
    + PySerial  (Configuration of IdeasX device over USB)

The Paho-MQTT mqttc module was modified (in a total hack-ish method). The mqttc does not provde the option to set a timeout for opening a socket. Therefore, if the user enters an incorrect IP / Port, the backend code (wsc_client.py) will hang in-definitly. Therefore, the following line was addded to client.py 
``` 
socket.setDefaultTimeout(1)
```

## List of Brokers 
The following link lists a number of publically available - free - brokers to support IdeasX. 
[https://github.com/mqtt/mqtt.github.io/wiki/public_brokers]

## Encoder Details / Notes 

### Switches 

0b110000000000001101100000001 10100

=======
## Workstation Client V2

This repository holds the first edition of the cross-platform supervisor software
used for IdeasX.

This software is written using the following:
+ Python3
+ PyQt5
+ Protocol Buffers

The following packages are required to run:
+ paho-mqtt
+ probably more...

Author(s): Tyler Berezowsky
>>>>>>> master
