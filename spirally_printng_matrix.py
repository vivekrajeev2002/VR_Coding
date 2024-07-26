mat = [[0]*3for i in range(4)]
re=3
rb=0
cb=0
ce=2
m=3
n=4
mat[0][0]=1
mat[0][1]=2
mat[0][2]=3
mat[1][0]=4
mat[1][1]=5
mat[1][2]=6
mat[2][0]=7
mat[2][1]=8
mat[2][2]=9
mat[3][0]=10
mat[3][1]=11
mat[3][2]=12

l=m*n
r=0
ar=[]

for i in range(len(mat)):
	for j in range(len(mat[0])):
		print(mat[i][j],"\t",end="")
	print()
print()
while(r<l):
	for i in range(cb,ce+1):
		print(mat[rb][i]);
		ar.append(mat[rb][i])
		r+=1
	rb=rb+1
	for i in range(rb,re+1):
		print(mat[i][ce])
		ar.append(mat[i][ce])
		r+=1
	ce=ce-1
	for i in range(ce,cb-1,-1):
		print(mat[re][i])
		ar.append(mat[re][i])
		r+=1
		
	re=re-1
	for i in range(re,rb-1,-1):
		print(mat[i][cb])
		ar.append(mat[i][cb])
		r+=1
	cb=cb+1
	
print(ar)
		



"""
	123
	456
	789
"""














