n=int(input())
l=list(map(int,input().split()))
d={}
a=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
for i in d:
    if d[i]>n//2:
        a=i
if a:
    print(1)
else:
    print(0)
    
