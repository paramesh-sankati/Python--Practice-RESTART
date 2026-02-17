lst=[1,2,4,5]

#summation
n=max(lst)  #or n =lst[-1]

missing_num= ((n*(n+1))//2)-sum(lst)
print(missing_num)

#or 
for i in range(1,max(lst)+1):
    if i not in lst:
        print(i)
        break

# XOR method
p=q=0
for i in range(len(lst)):
    p=p^lst[i]

natural_nums=range(1,len(lst)+2)
for j in range(len(natural_nums)):
    q=q^natural_nums[j]

print(p^q)

