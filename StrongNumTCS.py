#When the sum of factorial of individual digits of a number is equal to the original number the number is called a strong number. 

num=int(input("Enter Number:"))
org=num
def fact(n):
    if n==0:
        return 1
    elif n<0:
        return "Neg Numbers doesnt have factorials"
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact

s=0
while num>0:
    r=num%10
    s+=fact(r)
    num=num//10

if org==s:
    print("Strong Number")
else:
    print("Not a Strong Number")