x,y=list(map(int,input().split()))
z=(y+99)//100
if(z<=x):
    print("0")
else:
    print(z-x)
