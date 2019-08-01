from scapy.all import *

def TraceRoute():
	destNation = input("Enter the destination ip(IP/DNS):")
	pkt = IP(dst=destNation, ttl=(1,30))/ICMP()
	ans,unans = sr(pkt,timeout=2)
	ans.summary(lambda reply:reply[1].sprintf("%IP.src%"))

if __name__ == '__main__':
	TraceRoute()
