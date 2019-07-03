# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:18:48 2019

@author: 17pw04
"""
def validateIP(ip):
    if(ip>255 or ip<0):
        return -1
    else:
        return ip

def input_ip():
    ipv4 = []
    while True:
        try:
            ipv4 = list(map(int,(input().split('.'))))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        else:
            if(len(ipv4)==4):
                break
            else:
                print("Complete it")
    ipv4 = list(map(validateIP,ipv4))
    if(-1 in ipv4):
        return [0,0,0,0]
    else:
        return ipv4
    
def numberOfSubnets(subnet):
    final_sub = format(subnet[3],'08b')
    return 2**(final_sub.count('1'))

def numberOfHost(subnet):
    final_subnet = format(subnet[3],'08b')
    return 2**(final_subnet.count('0'))

def FormatSubnetID(subnet_id,host_id):
    for i in range(0,subnet_id):
        pass
    

def main():
    print('Enter the IP:')
    ipAddress = input_ip()
    print('Enter the SUBNET MASK:')
    subnet_mask = input_ip() 
    SubnetCount = numberOfSubnets(subnet_mask)
    print('Number of Subnets:',SubnetCount)
    HostCount = numberOfSubnets(subnet_mask)
    print('Host/Subnet:',HostCount)
    
if __name__=='__main__':
    main()