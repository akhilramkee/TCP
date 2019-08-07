import pandas as pd
import math
import random

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

def separateSegment(id,segmentSize,MTU):
	MTU = math.floor(MTU/8)*8
	totalsize = segmentSize
	currentAlloted = 0
	packet = []
	itr = id
	while(segmentSize):
		if(segmentSize<MTU):
			contentsize = segmentSize
			segmentSize = 0
			offset = currentAlloted/8
			currentAlloted +=segmentSize
			frag_bit = 0
		else:
			contentsize = MTU
			segmentSize-=MTU
			offset = currentAlloted/8
			currentAlloted+=MTU
			frag_bit = 1
		pc1 = {"identification":itr,"MDF":"00"+str(frag_bit),"offset":offset,"content":contentsize}
		packet.append(pc1)
	return packet


def main():
	segmentSize = 1
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
	minMTU = getMinMTU(sender,receiver,graph,router,routing_table)
	print("\nMinimumMTU:",minMTU)
	while(segmentSize != 0):
		segmentSize = int(input("Enter Segment size:"))
		Fragments = separateSegment(random.randint(1,2000),segmentSize,minMTU)
		print(Fragments)

if  __name__=='__main__':
	main()
