s=int(input("Enter the no of elements: "))
l=[]
for i in range(s):
    k=int(input("Enter the element:"))
    l.append(k)
larg=0
la=0
for i in l:
    if(i>larg):
        la,larg=larg,la
        larg=i
    
print("The second largest is:",la)