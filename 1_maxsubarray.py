
A=[-163,-20]
maxsofar =A[0]
curmax =0
flag=1
for i in range(0,len(A)):            
    curmax=max(A[i],A[i]+curmax)
    print("Value of curmax",curmax) 
    if(flag==1):
        maxsofar=curmax
        flag=0
    maxsofar=max(curmax,maxsofar)  
print(maxsofar)