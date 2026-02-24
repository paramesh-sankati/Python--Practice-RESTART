lst=list(map(int,input("Enter Numbers:").strip().split()))

#12 34 50 23 45
p1=0
p2=len(lst)-1

while p1<=p2:
    lst[p1],lst[p2]=lst[p2],lst[p1]
    p1+=1
    p2-=1

print(lst)

#using extra empty list 
res=[]
for i in lst[::-1]:
    res.append(i)

print(res)

#directly 
res2=lst[::-1]
print(res2)

#List comprehension
res3=[i for i in lst[::-1]]

print(res3)