import calendar
x=int(input())
if 1500<=x<=3000:
    if calendar.isleap(x):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
