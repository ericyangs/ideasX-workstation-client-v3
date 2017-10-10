# IdeasX Supervisor 

The purpose of this application is to provide an interface for therapists and care takers to configure and maintain devices in the IdeasX system. The application is cross platform and written in python3.X and PyQt (Qt5). The application currently has the following dependencies: 
    + Python 3.X 
    + PyQt (GUI)
    + Paho-MQTT (Network Communication)
    + PySerial  (Configuration of IdeasX device over USB)

The software is split into a few different files for sanity. 

**wsc_client.py** contains majority of the networking code for handling ideasX devices. 

**wsc_device.py** contains classes for each device in the IdeasX system to decode data recieved by the wsc\_client.py networking thread and commands which can be send to each device. 

**wsc_tools.py** contains helper tools created wsc\_io.py file (normally dumb things like converting a byte value from the wsc\_client into a percentage etc.)

**wsc_ui.py** contains the UI for the appication