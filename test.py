cache = [[None]*3 for i in range(3)]
cache[2][0]=99
cache[0][1]="Vivek"
for i in range(3):
    for j in range(3):
        print(cache[i][j],'   ',end='')
    print()

print(type(cache[1][0]))