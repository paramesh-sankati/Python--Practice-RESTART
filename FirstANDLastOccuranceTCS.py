def fl_occurance(arr,t):
    first_occurance,last_occurance=-1,-1

    for i in range(len(arr)):
        if arr[i]==t:
            first_occurance=i
            break

    for i in range(len(arr)-1,-1,-1):
        if arr[i]==t:
            last_occurance=i
            break

    return first_occurance,last_occurance

arr=list(map(int,input("Enter Array Elements:").strip().split(',')))
t=int(input('Target:'))

print(fl_occurance(arr,t))

