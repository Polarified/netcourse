# Lesson 3

### Connecting a Network
Let's think about how to connect a group of devices. We have cables, and can make up devices. What are our options?

* Cable - Connects two things. Layer 1.
* Repeater - Repeats a signal, because cables fade in strength. Layer 1.
* Hub - Repeater with more than just 2 ports. Sends everywhere. Layer 1.
* Switch - A smart Hub, that learns which device is where. Contains a MAC Address Table. Layer 2!

<h6> For Extras, go to the Lesson 2 Exercises. There are many interesting things to read about and learn!</h6>

### Finally, let's get tricky!
How can we read other people's packets in a Layer 2 network?

### Layer 2 Summary
The **data link layer** is responsible for allowing communication between **2 devices sharing a physical link**. 
It depends on the physical layer to actually send over the data, so that it can manage the **frames** it is sending over (groups of bits).
It handles the separation of bits into frames, error detection, flow control and collisions, as well as addressing of network cards.<br>
The data link layer gives the network layer (layer 3) the service of sending the data to the next link as needed, so that it can manage the passage of data over many hops (routing).

### Layer 3 - The Network Layer
The third layer of the OSI Model is the Network Layer. This part of the model is responsible for transferring packets across networks and from one network to another.
It also gives different points in the networks logical addresses in order to divide the network. These are called IP Addresses.

### IP Addresses
* Made of 4 bytes, 32 bits.
* A certain part of the address is the network identifier, and a certain part is the device identifier in the network. This is usually defined by a mask like so: /X. 
* 255 is reserved as a broadcast IP, which will be sent to the entire network. 

### How does routing work?
Each device that wants to send another device a packet, needs to find the way to send it there. The device doesn't know the entire way. It just wants to look if it is in the same link with it, or if it doesn't know a way to reach the device.
In this case, it will send to a router/gateway, which will try to find the way to the destination.

### How do we know the MAC of the device from the IP?
ARP!

### Let's make some packets!
Go to the lesson3.py file, and open up scapy documentation: https://scapy.readthedocs.io/en/latest/index.html