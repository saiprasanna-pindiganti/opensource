x,y,z=list(map(int,input().split()))
if(y>=z):
    print("0")
else:
    print((z-y)//x)
