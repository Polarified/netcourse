# Lesson 5

### Summary
We went over a few things so far:
* The Physical Layer
* The Data Link Layer
    * MAC Addresses
    * Devices (Switch, Hub)
* The Network Layer
    * IP Addresses
    * The idea of routing
    * ARP
* Network Tools
    * Wireshark (to sniff packets)
    * Scapy (to make packets)

Today, we will skip over some important things, just because I want to teach you something you can use and play around with before we finish.
For those of you that want to learn more, the things I would read about before moving on:
* Routing and Gateways
* NAT and the IPv4 Problem
* The idea of DNS
* The idea of DHCP

### The Network Layer, summarized:
The network layer, the third layer, is responsible for forwarding packets from end to end, between other routers and networks in the way.
It assumes the data link layer knows how to transfer data on each link, and concerns itself with the whole way. 

#### So, what is the next step?
Well, we usually have more than just one thing using the network on our computer.
If I have Google Chrome tabs open, and I'm asking Youtube to show me 2 different videos - how should my computer know which video to show on which tab? 
All it knows is that my IP - my 'identity' - asked for the videos.

### The Transport Layer
This means we need another piece of information. This piece is called a port.
Imagine your computers has 65535 little holes, each with a number. That is the port.
Each time you talk to someone over the network, you will tell them which port you exited, and which you want to reach on the other side.
You will listen on that port, expecting some kind of response.

The concept I just explained is called sockets. These are resources your computer uses to create network communication sessions, something more than just a simple packet and byebye.
There are 2 main different protocols that are used when we talk about this layer. We won't talk about them right now, because I want to do other things.

### Socket Programming!
Let's code some stuff with sockets!
