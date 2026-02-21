lst=[0,2,1,1,0,2,1,1,2]

#arrange it in 0,1,2 order without using sorting

#using count

res=[]
print(lst.count(1))

res.extend(lst.count(0)*[0])
res.extend(lst.count(1)*[1])
res.extend(lst.count(2)*[2])

print(res)

#using append
