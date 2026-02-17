#finding common letters in 2 strings 

str1='naina'
str2='reena'

print(set(str1).intersection(str2))

#or using & 
print(set(str1) & set(str2))

#else using loop

res=set()
for i in str1:
    if i in str2:
        res.add(i)

print(res)
