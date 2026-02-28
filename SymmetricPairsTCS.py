n=int(input("Enter no.of pairs :"))
pairs=[]
for i in range(n):
    pair=tuple(map(int,input("Enter Pair values:").strip().split(',')))
    pairs.append(pair)

print(pairs)

sym_pairs=[]

for i in pairs:
    if (i[1],i[0]) in set(pairs):
        sym_pairs.append((i[1],i[0]))

print(*sym_pairs)
    