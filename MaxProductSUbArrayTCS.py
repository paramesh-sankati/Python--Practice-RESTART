lst=list(map(int,input("Enter Numbers:").strip().split(',')))

max_product=float('-inf')
for i in range(len(lst)-1):
    prod=1
    for j in range(i+1,len(lst)):
        prod*=lst[j]
        max_product=max(max_product,prod)

    
print(max_product)
        
        


