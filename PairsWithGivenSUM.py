lst=[5,7,4,3,9,8,19,21]
s=12  #target sum =17
res=[]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==s:
            res.append((lst[i],lst[j]))

print(res)

#Else less tym complexity
left=0
right=len(lst)-1
lst.sort()
while(left<=right):
    if lst[left]+lst[right]>s:
        right-=1
    elif lst[left]+lst[right]<s:
        left+=1
    elif lst[left]+lst[right]==s:
        print(lst[left],lst[right])
        left+=1
        right-=1


