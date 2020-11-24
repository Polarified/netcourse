# Course Syllabus

### Goals:
- I want the students to understand how networks and the Internet allow us to communicate, as well as achieve fluency in speaking and thinking about networks.
- I want the students to feel confident in learning more about the technologies we will learn about, and go ahead and do it on their own! Be it through riddles (CTFs, Problem Solving, etc.) or creating new things (Web Apps, networking scripts and fun projects).
- I want the students to get accustomed to dealing with new things and problems when learning - develop resilience!<br>
### How to Achieve:
- I will give series of lectures about what makes the Internet work. The students will read about the different parts of the network and experiment with it. 
- We will go over the necessary technologies to master networks, be it CLIs, Python, Wireshark and more. Then, I will give suggestions for things to try and play with until the next session. We will talk about what certain people tried before each lesson!
- We will solve problems together during our sessions together. Things won't always be solved ahead of time! I will be trying things out with you, along with Google!



### The Course Contents:
<h5>Installations</h5>
- python, download at https://www.python.org/downloads/ (add to path, to make things easier)
- Any text editor/IDE. I will be using PyCharm for ease of running programs, I recommend Sublime. 
  https://www.jetbrains.com/pycharm/download/
  https://www.sublimetext.com/3
- pip (if you decided not to use an ide, in order to use packages) from https://phoenixnap.com/kb/install-pip-windows
- Wireshark, from https://www.wireshark.org/
- PuTTY from https://www.putty.org/


<h5>Python Basics</h5>
- Interpreted language
- Data types (int, float, string, boolean) and variables, duck typing
- input() and print(), string formatting
- Arithmetic Operators, Boolean operators, String methods syntax
- Conditionals syntax
- List (not array), Tuple. Mutability, reference vs value. List slicing
- for loop and while loop, enumerate, and other tricks
- Sets and Dicts
- Comprehensions
- Functions
- Objects

<h5>Networks</h5> 
- What is a Computer Network?
- What is it good for?
	- Sharing common resources, data, etc.
	- Communication, business, services
- The Boring Stuff
	- Architectures (p2p, client-server), Sizes, Topologies. Who cares?
- What is Communication in general?
- How to Organize this communication? Models!
- The OSI Model, in all it's glory. 

Layer 1
- Bits and Binary
- Modem
Layer 2
- NIC, MAC
- Switch, Hub
- NICs on our computer with ipconfig
- Dangers!
Layer 3
- IP, Router
- ARP
- Subnets and masks
- The IPv4 Problem and it's Solutions
	- IPv6
	- NAT
- Using Ping & ICMP
- Dangers?
Layer 4
- Ports!?
- TCP/UDP
	- netcat
- Sockets
	- netstat
- Socket Programming!
	- Simple echo server and client
- Packet Crafting with scapy
- nmap port scanning
- Dangers?
Layer 5
- All the protocols!
	- HTTP

https://www.javatpoint.com/computer-network-models


### Additional Materials, for those that want to explore!
<h5> Python </h5>
- *args & **kwargs
- Variable Scopes
- Exceptions and their handling
- lambda, map, filter
- itertools
- generators
- iterators
- Fluent Python, once you decide to become a pro... 
<h5> Beginner CTFs </h5>
- Bandit at https://overthewire.org/wargames/
- Basics at https://www.hackthissite.org/
- Python Challenge at http://www.pythonchallenge.com/
