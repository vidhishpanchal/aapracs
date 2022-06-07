#potential method
import math
from tabulate import tabulate
obj=[]
lst=[]
size=[]
amortized_cost=[]
actual_cost=[]
potential=[]
delta_potential=[]
while True:
  n=int(input())
  if n==0:
    break
  if len(obj)==0:
    obj.append(n)
    lst.append(n)
    size.append(len(obj))
    actual_cost.append(1)
    potential.append(2*len(lst)-len(obj))
  elif (math.log(len(lst),2)*10)%10==0:
    obj.extend([None]*len(lst))
    for i in range(len(obj)):
      if obj[i]==None:
        obj[i]=n
        actual_cost.append(len(lst)+1)
        lst.append(n)
        size.append(len(obj))
        potential.append(2*len(lst)-len(obj))
        break
  else:
    for i in range(len(obj)):
      if obj[i]==None:
        obj[i]=n
        actual_cost.append(1)
        lst.append(n)
        size.append(len(obj))
        potential.append(2*len(lst)-len(obj))
        break
for i in range(len(actual_cost)):
  if i==0:
    delta_potential.append(potential[i])
  else:
    delta_potential.append(potential[i]-potential[i-1])   
  amortized_cost.append(actual_cost[i]+delta_potential[i])
print(tabulate({'i':lst,'size':size,'actual cost':actual_cost,'delta potential':delta_potential,'amortized cost':amortized_cost},headers='keys'))