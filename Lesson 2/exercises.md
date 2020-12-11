# Lesson 2 Exercises

### Exercise 1 - The OSI Model (5 Layers):<br>
* Give a short answer about each layer - what does it need to do, and what does that allow the next level up to take for granted?<br>
\* Note: the OSI Model is 7 layers, but we will group 5, 6 & 7 together to Layer 5.
* Open Wireshark, and start sniffing. At the top, click the filter bar and write "icmp".
Now open a CMD window and ping google.com. <br>
Look at your sniffer. What do you see? Click one of the packets, and try to understand the layers. Which layers are there?

### Exercise 2 - Layer 1:<br>
Read about the Physical Layer of the OSI Model in Wikipedia (English or Hebrew).
* What types of physical media are there?
    * Which types do you have in/connecting to your house?
* Modulation: 
    * If you weren't in the online class - what is a Modem?
    * If you were, let's go deeper! 
        * What is Radio? Why do radio stations use modulation?
        * What is AM and FM? What's the difference?
* Situation - you have 2 cables and want to connect them to make a longer cable. What device can you use?
    * Imagine you could connect 2 cables by just putting them together and tying them. Why would you ever need the device from the previous question?

### Exercise 3 - Layer 2:<br>
Read about the Data Link Layer of the OSI Model in Wikipedia (English or Hebrew).
* What protocols do we have in the Data Link Layer? Which is the most common?
    * What are the different fields in an Ethernet frame?
    * On the cable, we have a stream of bits. How does Ethernet know when one frame ends and a new one begins?
* What is a MAC Address?
    * Find out what is your network card's MAC Address, two ways:
        * Send a ping and sniff it using Wireshark. 
        * Use a CMD command (find the right one :D )
    * What do the first 3 bytes of the MAC Address mean? What do the last 3 bytes mean?
        * Find out the company of your network card using Google.
    * What is a broadcast frame? How can you send a broadcast frame?
    * If somehow you received a packet that isn't for your MAC address (you aren't the destination MAC), what will your network card do?
        * Can you see it anyways? How?
* If we want to connect a device to multiple devices, how can we do it? Which devices can we use?
    * What is a Switch? What is a Hub? What's the difference?
    * What will a switch do if it gets a frame aimed at a previously unmet destination?
    
### Extras!
* What are loops in networks? How do switches avoid loops? (hint - STP)
* What are collisions in networks? How do switches reduce collision domains?
* A LAN is a local area network. What is a VLAN? What is it's purpose?
* What is a CRC?

If you are feeling like diving deeper into Layer 1, go ahead and read chapter 10 of the following pdf - https://data.cyber.org.il/networks/networks.pdf



