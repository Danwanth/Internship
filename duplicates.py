s=int(input("Enter the no of elements: "))
l=[]
for i in range(s):
    k=int(input("Enter the element:"))
    l.append(k)
for j in range(s):
    if l.count(j)>1:
        print(str(j)+" is a duplicate element of count",l.count(j))
        
