str="aabbsdfjmalayalam"
maxl=0
for i in range(0,len(str)):
    for t in  range(i,len(str)):
        temp=str[i:t+1]
        
        revtemp = temp[::-1]
        if(revtemp == temp):
           if(maxl<len(temp)):
                maxl = len(temp)
                print(temp)

print('Max length is ',maxl)         