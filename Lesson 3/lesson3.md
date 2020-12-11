# Lesson 3

### Connecting a Network
Let's think about how to connect a group of devices. We have cables, and can make up devices. What are our options?

* Cable - Connects two things. Layer 1.
* Repeater - Repeats a signal, because cables fade in strength. Layer 1.
* Hub - Repeater with more than just 2 ports. Sends everywhere. Layer 1.
* Switch - A smart Hub, that learns which device is where. Layer 2!

<h6> For Extras, go to the Lesson 2 Exercises. There are many interesting things to read about and learn!</h6>

### Finally, let's get tricky!
How can we read other people's packets in a Layer 2 network?

### Layer 2 Summary
The **data link layer** is responsible for allowing communication between **2 devices sharing a physical link**. 
It depends on the physical layer to actually send over the data, so that it can manage the **frames** it is sending over (groups of bits).
It handles the separation of bits into frames, error detection, flow control and collisions, as well as addressing of network cards.<br>
The data link layer gives the network layer (layer 3) the service of sending the data to the next link as needed, so that it can manage the passage of data over many hops (routing).

### Layer 3 - The Network Layer
For starters - IPs and the general idea of routing.
Then, ARP. 
Then, some scapy and arping! That's it.