n=int(input())
a=list(map(int,input().split()))
b=[0]*n
for i in range(n):
    lw=sum(a[:i]) if i>0 else 0
    rw=sum(a[i+1:]) if i<n-1 else 0
    b[i]=abs(lw-rw)
print(" ".join(map(str,b)))
