s=input("Enter Brackets  ")
l=[1]
for i in s:
    if(i=='('):
        l.insert(0,i)
    elif(i==')' and len(l)>1):
        l=l[1:]
    else:
        print("Not Balanced")
        quit()
if(len(l)==1):
    print("Balanced")
else:
    print("Not Balanced")