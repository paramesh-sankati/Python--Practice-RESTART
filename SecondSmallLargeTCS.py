lst=list(map(int,input("Enter Numbers:").strip().split()))

#Second largest 

largest=float('-inf')
for i in lst:
    if i > largest:
        largest=i

second_largest=lst[0]
for i in lst:
    if i>second_largest and i!=largest:
        second_largest=i
    

print(largest,second_largest)


#Second smallest
smallest=float('inf')
for i in lst:
    if i<smallest:
        smallest=i
    
second_smallest=lst[0]

for i in lst:
    if i<second_smallest and i!=smallest:
        second_smallest=i

print(smallest,second_smallest)
