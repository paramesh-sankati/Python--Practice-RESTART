#Frequency of words in a statement

s='one two three one four two one'
res=dict()
lst=s.split()
for i in lst:
    res[i]=lst.count(i)

print(res)


#Else
res2=dict()
for i in lst:
    if i not in res2:
        res2[i]=0
    res2[i]+=1

print(res2)