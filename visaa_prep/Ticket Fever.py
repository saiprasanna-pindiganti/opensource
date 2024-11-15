T=int(input())
for i in range(T):
    N,M=list(map(int,input().split()))
    if(N<=M):
        print("0")
    else:
        print(N-M)
