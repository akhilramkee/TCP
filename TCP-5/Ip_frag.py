import pandas as pd
import math

def getSystemName(client):
        while(1):
                system = input()
                if(system not in client):
                        print("Enter Valid address name:")
                else:
                        return system

def getMinMTU(sender,receiver,graph,router,routing_table):
        startHead = graph[sender][0]
        print(startHead,'->',end = "")
        currentHead = startHead
        destHead = graph[receiver][0]
        minMTU = 1000
        while(currentHead!=destHead):
                if(minMTU>routing_table[router.index(currentHead)]['MTU'][destHead]):
                        minMTU = routing_table[router.index(currentHead)]['MTU'][destHead]
                currentHead = routing_table[router.index(currentHead)]['route'][destHead]
                print(currentHead,'->',end="")
        print(receiver);return minMTU

def separateSegment(segmentSize,MTU):
	power8 = 8**0
	packet = {}
	itr = 0
	no_of_packets = math.ceil(segmentSize/MTU)
	contentsize = segmentSize + (no_of_packet-1)*20
	while(contentsize):
		pc1 = {"id":itr,"header":20,"content":


def main():
	client = ['client1','client2','client3','client4']
	router = ['A','B','C','D','E','F']
	graph = { 'client1':['A'],
		  'client2':['B'],
		  'client3':['E'],
		  'client4':['F'],
		  'A':['C','D'],
		  'B':['C'],
		  'C':['A','B','D','F'],
		  'D':['A','C','D'],
		  'E':['D','F'],
		  'F':['C','E']
		}
	routing_table = [{},{},{},{},{},{}]
	for i in range(1,7):
		data = pd.read_csv('routing'+str(i)+'.csv',index_col=0)
		routing_table[i-1] = data.to_dict()

	print("Enter Sender Name:")
	sender = getSystemName(client)
	print("Enter receiver Name:")
	receiver = getSystemName(client)
	segmentSize = input("Enter Segmentation Size:")
	minMTU = getMinMTU(sender,receiver,graph,router,routing_table)
	print("\nMinimumMTU:",minMTU)

if  __name__=='__main__':
	main()
