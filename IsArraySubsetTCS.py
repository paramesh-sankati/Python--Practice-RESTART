from collections import Counter

arr1=list(map(int,input("Enter Numbers:").strip().split(',')))
arr2=list(map(int,input("Enter Numbers:").strip().split(',')))


if Counter(arr1)<= Counter(arr2):
    print("Sub set")
else:
    print("Not a sub set")
    

