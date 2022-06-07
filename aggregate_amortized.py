n = int(input("Enter length : "))
a=[]
cost=0
op=0
for i in range(0, n):
    tmp=int(input(f"Enter number {i+1} : "))
    cost+=1
    a.append(tmp)
print(a)
li=[]
for i in range(0, n):
    size = len(li)
    if size>a[i]:
        op = op + 1
        cost = cost + 1
        for j in range(0, a[i]):
            cost+=1
            li.pop()
    else:
        cost+=1
        op+=1
        li.append(a[i])
print(li)
print(f"Time complexity : {cost}")
print(f"Number of operations : {op}")
print(f"Aggregate analysis : {cost/op}")



# ---------------------RAMI KA CODE-----------------------
cnt = 0
x = 0
a = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    tmp = int(input())
    a.append(tmp)
li = []
for i in range(n):
    sz = len(li)
    if sz > a[i]:
        x = x + 1
        cnt = cnt + 1
        for j in range(a[i]):
            cnt = cnt + 1
            li.pop()
            x = x + 1
            cnt = cnt + 1
    li.append(a[i])
print(li)
print("Total Complexity: " + str(cnt))
print("Number of operations: " + str(x))
print("Aggregate Analysis: " + str(cnt/x))

# print("-----------AGGREGATE ANALYSIS------------")
# n = int(input("Enter length of array : "))
# a=[]
# cost=0
# ops=0
# for i in range(0, n):
#     cost+=1
#     temp = int(input(f"Enter number {i+1} : "))
#     a.append(temp)
# print(f"Normal list : {a}")
# li=[]
# for i in range(0, n):
#     cost+=1
#     ops+=1
#     size=len(li)
#     if a[i]>size:
#         print(f"Since {a[i]}>{size}, we push {a[i]} in list.")
#         li.append(a[i])
#         cost+=1
#         print(f"List : {li}")
#     else:
#         ops+=1
#         for j in range(0, a[i]):
#             print(f"Since {a[i]}<{size}, we pop {a[i]} items from list")
#             li.pop()
#             cost+=1
#         print(f"List : {li}")
# print(f"Total Cost : {cost}")
# print(f"Total number of operations : {ops}")
# print(f"Amortized cost after Aggregate Analysis = cost/ops = {cost/ops}")
    
# cnt = 0
# x = 0
# a = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#  tmp = int(input())
#  a.append(tmp)
# li = []
# for i in range(n):
#  sz = len(li)
#  if sz > a[i]:
#      x = x + 1
#      cnt = cnt + 1
#      for j in range(a[i]):
#          cnt = cnt + 1
#          li.pop()
#          x = x + 1
#          cnt = cnt + 1
#          li.append(a[i])
# print(li)
# print("Total Complexity: " + str(cnt))
# print("Number of operations: " + str(x))
# print("Aggregate Analysis: " + str(cnt/x))