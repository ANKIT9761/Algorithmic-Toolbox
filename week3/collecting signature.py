n=int(input())
ar=[]
for i in range(n):
    a,b=map(int,input().split())
    ar.append((a,b))
i=0
count=0
s=set()
ar.sort()
while(i<n):
    l,r=ar[i][0],ar[i][1]
    i+=1
    count+=1
    while(i<n and ar[i][0]<=r):
        if(ar[i][1]<r):
            r=ar[i][1]
        i+=1
    s.add(r)
print(count)
print(*s)
    
