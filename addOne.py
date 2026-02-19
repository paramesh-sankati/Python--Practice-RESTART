#arr=[1,1,9,9,9,9,9,8,9,9,9]
arr=[9,9,9]
for i in range(-1,-len(arr)-1,-1):
    if arr[i]==9:
        arr[i]=0
    else:
        arr[i]+=1
        break
else:
    arr.insert(0,1)
print(arr)
