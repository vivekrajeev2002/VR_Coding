'''Given three sorted arrays A, B  and Cof not necessarily same sizes.
Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c
such that a, b, c be-longs arrays A, B, C respectively
'''
A = [ 1, 4, 5]
B = [ 6, 9, 15]
C = [ 2, 3, 6 ]
a=len(A)-1
b=len(B)-1
c=len(C)-1
n=min(a,b,c)

for i in range(n+1):
    aa = A[a]
    bb = B[b]  
    cc = C[c]
    dd = max(aa,bb,cc)
    if(dd==aa):
        A=A[:-1]
        a -= 1
    elif(dd==bb):
        B = B[:-1]
        b -= 1
    else:
        C = C[:-1]
        c -= 1
print(aa,bb,cc)
print(max(aa,bb,cc)-min(aa,bb,cc))