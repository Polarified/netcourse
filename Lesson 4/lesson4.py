# So, what did we learn?
# Take the following lines and put them in scapy and run them to try them out!
# To use scapy, run python and the line:
from scapy.all import *

# To create a simple IP packet:
ip_packet = IP()

# To view the contents of the packet:
print('Default IP Packet')
ip_packet.show()

# We can modify things in the packet by accessing their fields:
ip_packet.ttl = 128

# And use show again to see the difference:
print('IP Packet TTL 128')
ip_packet.show()

# If we want a more "full" packet, we can stack layers to add the Ethernet layer:
eth_ip_packet = Ether()/IP()
print('Default Ethernet + IP Packet')
eth_ip_packet.show()

# We can pass parameters while crafting to make it as we want it:
print('Ethernet with given src mac')
eth_packet = Ether(src='12:34:56:78:90:ab')
eth_packet.show()

# You can view packets in different formats:
# The following packet is an HTTP packet, that asks for the main page of facebook:
get_facebook=Ether()/IP(dst="www.facebook.com")/TCP()/"GET /index.html HTTP/1.0 \n\n"
# You can see it as a binary dump, or as the raw bytes alone.
print('======== Different Ways to look at Packets ==========')
print('Hexdump')
hexdump(get_facebook)
print('Raw')
print(raw(get_facebook))
# For more details:
print('Explanation of Fields')
ls(get_facebook)
# For less details (one line):
print('Summary')
print(get_facebook.summary())
# To see the details on the packet once it is assembled (checksum, length of the packet, etc.):
print('After Assembly and calculations')
get_facebook.show2()

# To make a group of packets (for example, to all devices in a network):
print()
print('Making groups of Packets')
packets_to_my_network = IP(dst="1.1.1.0/24")
print(packets_to_my_network.summary())
print([packet for packet in packets_to_my_network])

# To send a packet that we crafted (make sure to sniff with Wireshark and filter with icmp to see it!):
print("Sending packets")
ping_packet = IP(dst="1.1.1.1")/ICMP()/"The Ping will contains this message!"
send(ping_packet)

# To send and wait to receive one packet:
print("Sending and receiving once")
answer = sr1(ping_packet)
answer.show()

# To send and wait to receive answers forever or until you get all the answers:
print("Sending and receiving until got all answers")
answers, unanswered_packets = sr(IP(dst="1.1.1.1/30")/ICMP())
print(answers.summary())