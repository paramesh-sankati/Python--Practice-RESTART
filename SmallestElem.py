lst=list(map(int,input("Enter numbers:").strip().split()))

small=float('inf')

for i in lst:
    if i<small:
        small=i

print(small)

#Largest Number

largest=float('-inf')

for i in lst :
    if i>largest:
        largest=i

print(largest)