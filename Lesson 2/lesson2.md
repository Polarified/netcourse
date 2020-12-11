# Lesson 2

### Packets!
We are now going to take a look at some packets together in Wireshark. <br>
1. Close all your tabs and other network activity, and go to http://www.httpvshttps.com/, then open Wireshark. 
2. Choose the interface that has lines next to it (this means there are things to see, traffic is received), and start sniffing.
3. The things that are showing up are packets. Click one.
4. Explore! What do the different fields mean? What is in the headers? What is in the data?
5. Switch between http and https, and try to notice what changes.

### Packets are like onions...
* You may have noticed we have multiple layers to our packets.
* Each one is responsible for a different layer of abstraction.
* Lets go over what we need to have communication between 2 applications, on 2 different devices - a web client and server.


<h4> Bare Necessities </h4>

1. In order to pass information from one device to another, we need something physical to transmit data.
2. In order to connect the devices, we need them to be linked together - they must have some kind of connection between their network cards, to send data over.
3. If we have more than just 2 devices, we are going to want to logically group together devices into different networks. 
Not everything should be in the same network and be able to talk with everything. So the devices need to have some kind of logical identifier for themselves.
4. There can be many different applications on the device - how do we know which one is talking to which? The devices need to manage which service they are providing or connecting to.
5. We need to have some kind of protocol of how we communicate - what do we need to tell the other side? What does it need to know, and what do we expect to get as a response?

This is the OSI Model. If we go back to our Wireshark sniff, we can look at a packet and notice it is of this structure.<br>
Every time, the lowest layer will contain the next layers as it's data. This way we can have a packet that contains layers 1-3, but doesn't talk to a specific application/have a smarter protocol. <br>
If we want to add more, we simply put it in the data, and wrap it.

### Layer 1
* We aren't going to dive deep here, but it's important to understand that this layer just defines what electrical and physical things we expect in our relationship between our device and the medium of transmission.
* There are many things like the actual wiring, pins, voltage, adapters and more that matter here.
* The major functions provided are:
    1. Connecting and disconnecting from a medium
    2. Sharing the resources, flow control
    3. Modulation - converting between digital and analog signals. 


<h5> Self learning time! What is a Modem?</h5>


Enrichment:
* Modem == Modulator Demodulator.
* Responsible for translating between analog and digital signals, from the ISP to the digital one of our home network.
* Each home network usually has a modem, commonly included inside the box that we know as the router/modem.
* Questions:
    1. Why does the ISP speak analog?
    2. What is analog? How is it different from digital?
    3. Given: Analog signal can theoretically transfer infinite data. Why doesn't it?
    
### Layer 1 Summary
The **physical layer** is responsible for the **transmission of bits on a physical medium**. <br>
It gives the second layer the possibility to send entire frames, by handling the passage of data itself. The second layer doesn't care what type of media is used.
    
### Layer 2
So, we have a twisted pair cable / wifi / satellite / kiddie pool we can send waves over. 
Now what do we need?
* Framing - Sending packets as streams of 0s and 1s, and on the other side, breaking the stream of 0s and 1s into groups that make up the original packets.
* Addressing - We need to be able to determine who we are sending to. If we have a cable and 2 devices, this is easy. If we have many devices, we need a system.
* Error Control - Signals can get ruined. We need to check our signals for errors.
* Synchronization & Flow Control - We need to make sure the machines are talking to each other appropriately, at the same speed/capacity and each one after the other. Duplex is an issue here.

<h5> So there are many Layer 2 Protocols, right? </h5>


Well, kind of. But the main interesting one is Ethernet. <br>
<h6> Things might get kind of tricky here. Don't worry. </h6>
Ethernet is a computer networking technology used in networking. It is basically the standard for the data link layer, with a 48 bit MAC address, and the common Layer 3 Internet Protocol (IP) is commonly carried over it.
<br>
Mac Addresses - the 48 bit address used by Ethernet. It is unique per network interface controller (NIC). When sending to an address, you can send to a single address, to a group of addresses, or to everyone. The first three bytes are the vendor (manufacturer), the last three are anything.
Ultimately, you don't really know where you are sending. Any address can intercept the packet. The question is whether a device wants to read it or not.<br>
What if we want to read packets that aren't aimed at us? We can use promiscuous mode.
