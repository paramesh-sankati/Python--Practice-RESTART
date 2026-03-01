num=int(input("Enter num:"))
org=num
rev=0
while num>0:
    last_digit=num%10
    rev=rev*10+last_digit
    num=num//10

if org==rev:
    print("Palindrome")
else:
    print("Not a palindrome")

