num=int(input("Enter Num:"))
num_sq=num**2

print("Atomorphic") if str(num_sq).endswith(str(num)) else print("Not An Atomorphic")