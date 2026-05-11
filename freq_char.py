s=input("Enter the string to find freq of: ")
l=[]
for i in s:
    if(i not in l):
        print("The frequency of chara "+i+" is: ",s.count(i))
        l.append(i)
    else:
        continue