def maj_element(arr):
    dici={}
    for i in arr:
        if i not in dici:
            dici[i]=1
        else:
            dici[i]+=1

    for k,v in dici.items():
        if v>len(arr)//2:
            return k
        
    return -1


arr=list(map(int,input("Enter Numbers:").strip().split(',')))
print(maj_element(arr))
