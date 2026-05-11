import math
s=int(input("Enter the dimensions of vector: "))
l1,l2=[],[]
for i in range(s):
    k=int(input("Enter the vector component of u:"))
    l1.append(k)

for i in range(s):
    k=int(input("Enter the vector component of v:"))
    l2.append(k)

sum=0    
for j in range(s):
    sum+=l1[j]*l2[j]
    
if(sum==0):
    print("orthogonal")
else:
    print("not")