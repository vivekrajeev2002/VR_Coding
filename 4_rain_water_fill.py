A=[ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 ]
sumn=0
lf=[]
rf=[]
t=0
j=0
l=len(A)
m1 = A[0]
m2=A[l-1]
for i in range(l):
    if(A[i]>m1):
        m1 = A[i]
    lf.append(m1)
    if(A[l-i-1]>m2):
        m2 = A[l-i-1]
    rf.append(m2)
rf=rf[::-1]
for i in range(l):
    temp = A[i]
    t=lf[i]
    j=rf[i]
    sumn = sumn + min(t,j) - temp
print("Water filled is ",sumn)