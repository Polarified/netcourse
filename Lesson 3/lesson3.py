# scapy basics
from scapy.all import *


def arp_scan(ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
    ans, unans = srp(request, timeout=2, retry=1)
    result = []
    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})
    return result


result = arp_scan('10.100.102.0/24')
print(result)
