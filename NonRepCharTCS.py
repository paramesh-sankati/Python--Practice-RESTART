'''def non_rep_char(s):
    for i in range(len(s)):
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return s[i]
    else:
        return -1
    

s=input("Enter string:")

print(non_rep_char(s))'''

def non_rep_char(s):
    dici={}
    for i in s:
        if i not in dici:
            dici[i]=1
        else:
            dici[i]+=1

    for k,v in dici.items():
        if v==1:
            return k
    else:
        return -1

s=input("Enter input string:")

print(non_rep_char(s))