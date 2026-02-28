rows,cols=map(int,input("Enter Rows,cols:").strip().split(','))

matr=[]
for i in range(rows):
    row=list(map(int,input(f"Enter {i} row elements: ").strip().split(',')))
    matr.append(row)

print(matr)

for i in range(rows):
    for j in range(cols):
        print(matr[j][i],end=" ")
    print()