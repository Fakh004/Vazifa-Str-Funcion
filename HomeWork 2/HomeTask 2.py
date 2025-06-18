n = [1, 2, 2, 3, 3,3]
fakh={}
for i in n:
    fakh[i]=fakh.get(i,0)+1
print(fakh) 