import math
stri=input()
r=[]
c=1
for i in range(1,len(stri)):
    if stri[i]==stri[i-1]:
        c+=1
    else:
        r.append(stri[i-1]+str(c))
        c=1
r.append(stri[-1]+str(c))
print(''.join(r))
