
from sys import argv
from scapy.all import *
from scapy.layers.inet import Ether

def printf(s,r):
    r.sprintf("%Ether.src% %ARP.psrc%")

def arp_ping(host):
    """ARP Ping"""

    # The fastest way to discover hosts on a local ethernet network is to use the ARP Ping method:
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=host), timeout=2)

    # Answers can be reviewed with the following command:
    ans.summary(lambda kv:kv[1].sprintf("%Ether.src% %ARP.psrc%"))

if __name__ == '__main__':
    arp_ping(argv[1])
