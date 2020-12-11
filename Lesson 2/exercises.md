Exercise 1 - The OSI Model (5 Layers):<br>
Give a short answer about each layer - what does it need to do, and what does that allow the next level up to take for granted?<br>
\* Note: the OSI Model is 7 layers, but we will group 5, 6 & 7 together to Layer 5.


Exercise 2 - Layer 1:<br>
Read about the Physical Layer of the OSI Model in Wikipedia (English or Hebrew).
* What types of physical media are there?
    * Which types do you have in/connecting to your house?
* Modulation: 
    * If you weren't in the online class - what is a Modem?
    * If you were, let's go deeper! 
        * What is Radio? Why do radio stations use modulation?
        * What is AM and FM? What's the difference?
* Situation - you have 2 cables and want to connect them to make a longer cable. What device can you use?


Exercise 2:<br>
a. Go to another device that is connected to your wifi. Look up it's ip using ipconfig.<br>
If it has more than one network card, choose the one that is connected to the home wifi.<br>
b. Go back to your computer, and try to ping the other computer! Did it work?<br>
c. Spoiler - your home wifi IP addresses probably look something like ???.???.???.x, and x starts from 1 and goes up. 
Send pings to devices on your home wifi, starting at ???.???.???.1 and going up, until you don't get a response. For example, you try 10.10.10.1, 2, 3 and then fail at 4.<br>
d. Now connect your phone to the home wifi. Try to ping ???.???.???.4, or ???.???.???.x where x is what you failed at.<br>
Did you get a response? Why?
<br>

Exercise 3:<br>
For the brave: look around the internet for a tool called netcat/ncat/nc. Use it to make a simple chat between 2 computers in your house, or between 2 cmd windows in your computer.<br>