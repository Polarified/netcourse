import pprint
from scapy.all import *


def ping_your_router(home_network_ip, text, timeout):
    """
    Send a ping to your router, with text of your choice, and show it's response!
    :param home_network_ip: the first 3 bytes of your router's IP, which is also your home IP. For example: 'x.x.x'
    :param text: the text you want for your ping
    :param timeout: the amount of time to wait for a response from the router before giving up
    """
    # Your router is almost always the first IP in the network, so x.x.x + .1
    router_ip = home_network_ip + ".1"
    # Send and receive one answer to your ping.
    response = sr1(IP(dst=router_ip) / ICMP() / text, timeout=timeout)
    # If we didn't get a response after "timeout" seconds, print a failure message...
    if response is None:
        print('Got no response, maybe your router is down?')
    # If we got a response, great! Show it!
    else:
        response.show()


def ping_scan(network_to_scan, timeout):
    """
    A Ping Scanner is a piece of code that sends ping to devices and waits to see if they answer in order to know if they exist in your network.
    Make your scanner print a nice list of which IPs are alive and answered your request.
    Experiment with turning devices in your house on and off and seeing if they answer your ping scanner!!

    :param network_to_scan: the network ip to scan. Should be something of the type: x.x.x.x/X
    :param timeout: the amount of time to wait before giving up on the responses and assuming the device isn't there.
    """
    ans, unans = sr(IP(dst=network_to_scan) / ICMP(), timeout=timeout)
    print(ans.summary(lambda s, r: r.sprintf("%IP.src% is alive")))


def arp_scan(network_to_scan, timeout, retry):
    """
    An ARP Scanner is a piece of code that sends ARPs to devices and waits to see if they answer in order to know if they exist in your network.
    Make your scanner print a nice list of which IPs are alive and answered your request, and maybe even include what their MAC is!
    Experiment with turning devices in your house on and off and seeing if they answer your arp scanner!!

    :param network_to_scan: the network ip to scan. Should be something of the type: x.x.x.x/X
    :param timeout: the amount of time to wait before giving up on the responses and assuming the device isn't there.
    :param retry: how many times to retry before giving up...
    """
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network_to_scan)
    pprint.pprint(request)
    ans, unans = srp(request, timeout=timeout, retry=retry)
    result = []
    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})
    pprint.pprint(result)


def traceroute(destination, max_ttl, timeout):
    """
    Write the program traceroute, that prints all the IPs between you and the target ip, by sending ICMP messages!
    :param destination: the ip to trace the route for
    :param max_ttl: the maximum ttl to give, so you know when to stop
    :param timeout: the amount of time to wait for replies
    """
    answered, unanswered = sr(IP(dst=destination, ttl=(1, max_ttl)) / ICMP(), timeout=timeout)
    hops = {}
    for sent, received in answered:
        if received.src in hops.values():
            break
        hops[sent.ttl] = received.src
    print('Route from {} to {}'.format(answered[0][0].src, destination))
    pprint.pprint(hops)



TABLE = {(64, 5840): 'Linux 2.4/2.6',
         (64, 5720): 'Google Linux',
         (64, 65535): 'FreeBSD',
         (128, 65535): 'Windows XP',
         (128, 8192): 'Windows 7, Vista and Server 2008',
         (255, 4128): 'Cisco Router', }


def os_detection(count):
    """
    Sniff TCP packets on your network and return what operating system (Windows, Linux, etc.) each IP you see is!
    :param count: how many packets to collect.
    :return: a dict that contains pairs of the type: {'1.1.1.1': 'Windows', '2.2.2.2': 'Linux'}
    """
    load_module("p0f")
    fil = "tcp[tcpflags] & (tcp-syn) != 0"
    packets = sniff(filter=fil, count=count)
    result = {}
    for packet in packets:
        pass


# Need to write cases...


# ping_your_router('10.100.102', "Hello there!", 2)
# ping_scan('10.100.102.0/24', 2)
# arp_scan('10.100.102.0/24', 2, 1)
traceroute("172.217.169.78", 20, 3)
# os_detection(2)
