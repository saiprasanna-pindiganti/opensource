N,m=list(map(int,input().split()))
n=list(map(int,input().split()))
d=[]
nd=[]
for i in range(N):
    if(n[i]%m==0):
        d.append(n[i])
    else:
        nd.append(n[i])
print(sum(d)-sum(nd))
    
