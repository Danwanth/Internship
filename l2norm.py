import math
s=int(input("Enter the no of elements: "))
l=[]
for i in range(s):
    k=int(input("Enter the vector component:"))
    l.append(k)
sum=0
for i in l:
    sum+=i**2

print("The L2 norm is: ",math.sqrt(sum))
    