"""
The exercises are of the type where I give you a function to fill in, and you need to make it work!
"""


# Think - how can you find your router's IP?
def ping_your_router(home_network_ip, text, timeout):
    """
    Send a ping to your router, with text of your choice, and show it's response!
    :param home_network_ip: the first 3 bytes of your router's IP, which is also your home IP. For example: 'x.x.x'
    :param text: the text you want for your ping
    :param timeout: the amount of time to wait for a response from the router before giving up
    """


# Break the problem down into pieces:
# 1. How can we make all the different packets to send?
# 2. How can we send and receive all our packets at once?
# 3. How can we print the responses in a nice way to see which devices exist and which don't?
def ping_scan(network_to_scan, timeout):
    """
    A Ping Scanner is a piece of code that sends ping to devices and waits to see if they answer in order to know if they exist in your network.
    Make your scanner print a nice list of which IPs are alive and answered your request.
    Experiment with turning devices in your house on and off and seeing if they answer your ping scanner!!

    :param network_to_scan: the network ip to scan. Should be something of the type: x.x.x.x/X
    :param timeout: the amount of time to wait before giving up on the responses and assuming the device isn't there.
    """


# This next exercise is very similar, yet it might not work if you aren't careful.
# Hint: what is the difference between send and sendp? Or sr and srp?
def arp_scan(network_to_scan, timeout):
    """
    An ARP Scanner is a piece of code that sends ARPs to devices and waits to see if they answer in order to know if they exist in your network.
    Make your scanner print a nice list of which IPs are alive and answered your request.
    Experiment with turning devices in your house on and off and seeing if they answer your arp scanner!!

    :param network_to_scan: the network ip to scan. Should be something of the type: x.x.x.x/X
    :param timeout: the amount of time to wait before giving up on the responses and assuming the device isn't there.
    """


def traceroute(destination, max_ttl):
    """
    Write the program traceroute, that prints all the IPs between you and the target ip!
    :param destination: the ip to trace the route for
    :param max_ttl: the maximum ttl to give, so you know when to stop
    """

# CHALLENGE
# Use the ttl_window.png file to figure out what changes for each operating system!
def os_detection(count):
    """
    Sniff TCP SYN packets on your network and return what operating system (Windows, Linux, etc.) each IP you see is!
    :param count: how many packets to collect.
    :return: a dict that contains pairs of the type: {'1.1.1.1': 'Windows', '2.2.2.2': 'Linux'}
    """
    # Hint: to sniff TCP, use "tcp" as your filter when sniffing!
    # Don't worry about what TCP is, we will learn next time.
