arr=list(map(int,input("Enter numbers :").strip().split(',')))

dici={}
for i in arr:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1

#sorted_dici=dict(sorted(dici.items(),key=lambda x:x[1],reverse=True))

sorted_arr=sorted(arr,key=lambda x:(-dici[x],x))

print(sorted_arr)


    