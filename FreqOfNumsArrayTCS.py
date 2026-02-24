lst=list(map(int,input("Enter Numbers:").split()))

dici=dict()

for i in lst:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1

for k,v in dici.items():
    print(k,v)