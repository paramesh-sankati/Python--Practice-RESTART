s=input("Enter input string:")

dici={}
for i in s:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
    

res_sum=0
for k,v in dici.items():
    if v%2==0:
        res_sum+=v

print(res_sum)
