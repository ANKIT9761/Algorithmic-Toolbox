n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
su=0
for i in range(n):
    su+=a[i]*b[i]
print(su)
