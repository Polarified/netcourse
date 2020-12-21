# Lesson 3

### Connecting a Network
Let's think about how to connect a group of devices. We have cables, and can make up devices. What are our options?

* Cable - Connects two things. Layer 1.
* Repeater - Repeats a signal, because cables fade in strength. Layer 1.
* Hub - Repeater with more than just 2 ports. Sends everywhere. Layer 1.
* Switch - A smart Hub, that learns which device is where. Contains a MAC Address Table. Layer 2!

<h6> For Extras, go to the Lesson 2 Exercises. There are many interesting things to read about and learn!</h6>

### Let's get EVIL!
How can we read other people's packets in a Layer 2 network?

### Layer 2 Summary
The **data link layer** is responsible for allowing communication between **2 devices sharing a physical link**. 
It depends on the physical layer to actually send over the data, so that it can manage the **frames** it is sending over (groups of bits).
It handles the separation of bits into frames, error detection, flow control and collisions, as well as addressing of network cards.<br>
The data link layer gives the network layer (layer 3) the service of sending the data to the next link as needed, so that it can manage the passage of data over many hops (routing).

### Layer 3 - The Network Layer
The third layer of the OSI Model is the Network Layer. This part of the model is responsible for transferring packets between two **entities**.
It also gives different points in the networks logical addresses in order to divide the network into smaller networks. These are called IP Addresses.

### IP Addresses
* Made of 4 bytes, 32 bits. (How many IPs can we represent?)
* A certain part of the address is the network identifier, and a certain part is the device identifier in the network. This is usually defined by a mask like so: /X or like so 255.255.255.0 (for example).
* A broadcast address is the highest device number in the network. For example - in the network 192.168.16.0 with a subnet mask of 255.255.255.0, the broadcast address is 192.168.16.255.

###### Subnet Mask example time!

### Understanding the point!
The Data Link Layer deals with sending between two devices that share a physical link and are in the same network. The Network Layer needs to string together many connections, in order to connect devices that aren't connected by themselves. 

###### Draw.io example time!

#### How do we know the MAC?
Take a moment to think - we want to send to ip x, how do we send if we don't know the MAC?

### ARP - Address Resolution Protocol
* Our first real protocol!
* Send a broadcast frame containing the wanted destination IP, from the source IP and MAC.
* The holder of the IP will send it's MAC back as a unicast packet.
* All devices hold an ARP Cache (table) that keeps IP-MAC pairs.