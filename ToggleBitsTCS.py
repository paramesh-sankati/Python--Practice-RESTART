
n=int(input("Enter number:"))

bin_form=bin(n)
lst=[i for i in str(bin_form)[2:]]

res_bin='0b'
for i in lst:
    print(i)
    if i=='0':
        res_bin+='1'
    else:
        res_bin+='0'

print(int(res_bin,2))