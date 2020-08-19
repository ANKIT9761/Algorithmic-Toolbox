n=int(input())
a=[0]*(n+1)
for i in range(1,n+1):
    if i>=4:
        a[i]=min(a[i-4]+1,a[i-3]+1,a[i-1]+1)
    elif i==3:
        a[i]=min(a[i-3]+1,a[i-1]+1)
    else:
        a[i]=a[i-1]+1
print(a[n])
