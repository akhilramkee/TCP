from sys import argv

from scapy.all import *
from scapy.layers.inet import IP, ICMP


def icmp_ping(host):
    """ ICMP Ping """

    data = 'University'
    # Classical ICMP Ping can be emulated using the following command:
    ans, unans = sr(IP(dst=host)/ICMP()/Raw(load = data),timeout=2)

    # Information on live hosts can be collected with the following request:
    for s,r in ans:
         l = r[Raw].load
         print(l)

if __name__ == '__main__':
    icmp_ping(argv[1])
