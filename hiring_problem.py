import random
print("------------RANDOMIZED HIRING PROBLEM--------------")
n = int(input("Enter the number of candidates : "))
li=[]
for i in range(0,n):
    li.append(random.randint(1, 50))
print(f"List of candidates with scores : {li}")
interviewcost=10
hiringcost=50
totalcost=0
salaryperday=100
noofdaysworked=0
best=0
for i in range(0, len(li)):
    totalcost+=interviewcost
    if li[i]>best:
        print(f"Person with score {best} has been fired, payed {noofdaysworked*salaryperday}")
        totalcost+=(noofdaysworked*salaryperday)
        best=li[i]
        print(f"Person with score {li[i]} is hired !")
        totalcost+=hiringcost
        noofdaysworked=1
    else: 
        noofdaysworked+=1
        # totalcost+=salaryperday
        print(f"Day {noofdaysworked} of Person With Score {best}")
print(f"Total Cost : Rs. {totalcost}")


