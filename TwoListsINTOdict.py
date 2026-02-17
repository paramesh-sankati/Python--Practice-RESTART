#Converting 2 lists into Dictionary

lst1=['Naina','Shana','Jin']
lst2=[12,23,45]
print(dict(zip(lst1,lst2)))

#Else

dici=dict()
c=0
for i in lst1:
    dici[i]=lst2[c]
    c+=1

print(dici)