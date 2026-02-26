lst=list(map(int,input("Enter numbers:").strip().split()))
rep_ele=[]
for i in range(len(lst)):
    if lst[i] in lst[i+1:]:
        rep_ele.append(lst[i])

print(rep_ele)