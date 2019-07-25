# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def validate(ip):
    if(ip>255 or ip<0):
        return -1
    else:
        return ip

def returnClass(ip):
     if(all(ip_part == 0 for ip_part in ip)):
         return 'Special Address:0.0.0.0'
     elif(all(ip_part == 1 for ip_part in ip)):
         return 'Special Address:1.1.1.1'
     elif(all(ip_part==255 for ip_part in ip)):
         return 'Broadcast address'
     elif(ip[0]==10 or ip[0]==172 or ip[0]==169):
         return 'Special Address : Local Network'
     else:
         if(ip[0]>=0 and ip[0]<128):
             return 'Class A'
         elif(ip[0]>=128 and ip[0]<192):
             return 'Class B'
         elif(ip[0]>=192 and ip[0]<224):
             return 'Class C'
         elif(ip[0]>=224 and ip[0]<240):
             return 'Class D'
         elif(ip[0]>=240 and ip[0]<256):
             return 'Class E'
     
def main():
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
                
    ipv4_valid = list(map(validate,ipv4))
    if(-1 in ipv4_valid):
        print('Invalid ip')
    else:
        print(returnClass(ipv4))
        
if __name__=='__main__':
    main()
    