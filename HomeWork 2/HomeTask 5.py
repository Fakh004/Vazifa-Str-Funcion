words=['apple','banana','kiwi']

string=''.join(words)
dict1={}
for i in string:
    cnt=0
    for j in string:
        if i==j:
            cnt+=1
    dict1[i]=cnt
print(dict1)