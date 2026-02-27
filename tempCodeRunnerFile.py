lst=[1,5,8,15,8,25,9]
temp=sorted(list(set(lst)))
dici={}
for i,v in enumerate(temp):
    dici[v]=i+1
print(dici)

res=[]
for i in lst:
    res.append(dici[i])

print(res)