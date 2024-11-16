n=int(input())
sp=[3,4,5]
su=[6,7,8]
au=[9,10,11]
wi=[12,1,2]
if(1<=n<=12):
    if(n in sp):
        print("Spring")
    elif(n in su):
        print("Summer")
    elif(n in au):
        print("Autumn")
    else:
        print("Winter")
else:
    print("Invalid")
