#accounting method
import math
from tabulate import tabulate
obj=[]
lst=[]
cost=[]
cost1=[]
size=[]
while True:
	n=int(input())
	if n==0:
		break
	if len(obj)==0:
		lst.append(n)
		obj.append(n)
		size.append(len(obj))
		cost.append(1)
		cost1.append(3)
	elif (math.log(len(lst),2)*10)%10==0:
		temp=[None]*len(lst)
		obj.extend(temp)
		# print(len(obj))
		for i in range(len(obj)):
			if obj[i]==None:
				obj[i]=n
				cost.append(len(lst)+1)
				lst.append(n)
				cost1.append(3)
				size.append(len(obj))
				break
	else:
		for i in range(len(obj)):
			if obj[i]==None:
				obj[i]=n
				lst.append(n)
				cost.append(1)
				cost1.append(3)
				size.append(len(obj))
				break
	
bank=[]
val=0
for i in range(len(cost)):
  bank.append(val+cost1[i]-cost[i])
  val=val+cost1[i]-cost[i] 
print(tabulate({'i':lst,'size':size,'cost':cost,'amortized cost(cost 1)':cost1,'bank':bank},headers='keys'))