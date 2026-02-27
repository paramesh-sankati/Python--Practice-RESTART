'''def Equ_ind(arr):
    for i in range(1,len(arr)):
        if sum(arr[:i])==sum(arr[i+1:]):
            return i
    else:
        return -1
    

arr=list(map(int,input("Enter arr elements:").strip().split(',')))

print(Equ_ind(arr))
'''

def equ_ind(arr):
    left_sum=0
    total_sum=sum(arr)
    for i in range(len(arr)):
        right_sum=total_sum - left_sum -arr[i]
        if left_sum==right_sum:
            return i
        left_sum+=arr[i]

    else:
        return -1
    
arr=list(map(int,input("Enter array Ele:").strip().split(',')))
print(equ_ind(arr))
    


        