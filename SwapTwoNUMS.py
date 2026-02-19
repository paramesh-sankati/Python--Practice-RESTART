#using +,- operators
a=10
b=12
a=a+b  #22
b=a-b  #22-12=10
a=a-b    #22-10=12
print(a,b)

#Else using XOR operator
p=10
q=12
p=p^q
q=p^q
p=p^q
print(p,q)

#simple way
a,b=b,a
print(a,b)

#using third var
temp=a
a=b
b=temp
print(a,b)