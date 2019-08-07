def getipv4(s):
	k = []
	for i in range(28,len(s),2):
		k.append(s[i:i+2])
	if(k[0][1]):
		size = int(k[0][1])*4
	return k[0:size]

def parse_type(string):
	if(int(string)==4):
		return "IPv4"

def parse_hlen(string):
	return int(string)*4

def parse_service(string):
	return string

def parse_length(string):
	return int(string,16)

def parse_identification(string):
	return int(string,16)

def parse_flag(string):
	string = format(int(string[0]),'04b')
	if(int(string[1]) == 1):
		return "Do not fragment"
	elif int(string[2]) == 1:
		return "More Fragments:true"
	elif int(string[2]) == 0:
		return "More Fragments:false"

def offset_frag(string):
	string = string[3:]
	return int(string,16)

def ttl(string):
	return int(string,16)

def protocol(string):
	switcher = {
		1:"ICMP",
		4:"IP",
		6:"TCP",
		17:"UDP"
	}
	return switcher.get(int(string),"Need to find")

def checksum(string):
	return "0x"+string

def ip_parse(s1,s2,s3,s4):
	return str(int(s1,16))+"."+str(int(s2,16))+"."+str(int(s3,16))+"."+str(int(s4,16))

def parse_ipv4(packet):
	packet_structure = {}
	packet_structure["type"] = parse_type(packet[0][0])
	packet_structure["hlen"] = parse_hlen(packet[0][1])
	packet_structure["service_type"] = parse_service(packet[1])
	packet_structure["total_length"] = parse_length(packet[2]+packet[3])
	packet_structure["identification"] = parse_identification(packet[4]+packet[5])
	packet_structure["flags"] = parse_flag(packet[6])
	packet_structure["offset_frag"] = offset_frag(packet[6]+packet[7])
	packet_structure["Time-to-live"] = ttl(packet[8])
	packet_structure["Protocol"] = protocol(packet[9])
	packet_structure["Checksum"] = checksum(packet[10]+packet[11])
	packet_structure["Source IP"] = ip_parse(packet[12],packet[13],packet[14],packet[15])
	packet_structure["Destination Ip"] = ip_parse(packet[16],packet[17],packet[18],packet[19])
	return packet_structure

def getARP(streamdata):
	k = []
	for i in range(28,len(streamdata),2):
		k.append(streamdata[i:i+2])
	return k

def main():
	f = open('arp','r')
	streamdata = f.read()
	if(streamdata[24:28] == '0800'):
		packet = getipv4(streamdata)
		print(parse_ipv4(packet))
	elif(streamdata[24:28]=='0806'):
		packet = getARP(streamdata)
		print(packet)

if __name__=='__main__':
	main()
