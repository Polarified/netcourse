# Lesson 1
### What are computer networks?
A computer network is a group of devices, using common communication protocols, over certain media, to exchange information.
<br>
<h5> What networks do you know about? </h5>

### Why do we care?
Networks allow us to do a lot of different important things.<br>
For example: 
- Look at pictures on Instagram
- Read and write emails
- Have Zoom calls
- Buying clothes online
- Do complicated computations with distributed computing
- Share files


And much much more. <br>

### How does it work?
Lets try and take a look at what happens when we go to a site, for example, google.com.<br>
Google gives us a search engine. This means it looks at all the servers that connect themselves to the Internet, and collects their pages. Then it tries to understand the page and when I search, it shows me pages that match my search.<br>
<h5>But how do we get to Google?</h5>
1. Let's use Paint and Google Chrome to see a diagram of the network, how a client-model works.

2. Now, lets use ping to send something to google.com, and get a response!
3. Let's go back to our diagram, and make it bigger and better! And what are those numbers? IP Addresses!
4. Let's use tracert to take a better look at what we sent google.com.
5. Now, let's try to figure out what our own ip is!

Hopefully now we better understand the internet. But networks don't have to be Internet! <br>

- A network can be peer to peer or client-server
- A network can be of many different sizes
- A network can send different kinds of data
- A network can be connected in many different ways


All of this doesn't matter, because **what truly matters is that there are a group of devices that communicate a certain way.** We want to understand how they do this, so we can program things to do it, or look at other programs that do it and figure them out (for whatever reason).
The way this happens in digital networks is with **packets**, which are just groups of information, organized according to the **OSI Model**. It's a decision of how to communicate, just like our language is. That stuff is going to happen in the next lessons. <br>

### Installations
We are going to need tools, so let's install them together. The links are in syllabus.md.<br>
Once we are all installed, let's start going over some of the things we are going to use.
- Wireshark is a packet sniffer. It lets us look at packets that our computer gets.
- Python is a programming language that is super easy to start using, but also very powerful. It's very easy to play around with networks with Python, as well as make some very complicated programs.
- pip is a package manager that allows us to get more packages that didn't come with the basic Python installation. 
- PyCharm is an IDE (Integrated Development Environment), meaning a text editor that also can run the program.
- Sublime is a text editor, so it can't run the program. But using Python we can run files just the same, from the command line.


### Packets!
We are now going to take a look at some packets together in Wireshark. <br>
1. Go to http://www.httpvshttps.com/, and then open Wireshark. 
2. Choose the interface that has lines next to it, and start sniffing.
3. The things that are showing up are packets. Click one.
4. Explore! What do the different fields mean? What is in the headers? What is in the data?


We will learn all about these things in the future. This is just a taste, so we feel comfortable with Wireshark.

### Snakes!
We are now going to go over some Python and understand the language and how easy it is to code with it.
The syllabus outlines everything, and the code will document what we did at basics.py.

 






