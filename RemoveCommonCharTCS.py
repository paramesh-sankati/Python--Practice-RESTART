s1=input("Enter string-1 :")
s2=input("Enter string-2 :" )

common=set(s1) & set(s2)

res=''
for i in s1:
    if i not in common:
        res+=i

if len(res)==0:
    res=s1

print(s1)