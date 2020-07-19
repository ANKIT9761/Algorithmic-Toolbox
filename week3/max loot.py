n,weight=map(int,input().split())
di={}
for i in range(n):
    a,b=map(int,input().split())
    di[a/b]=b
di=sorted(di.items(),reverse=True)
i=0
pr=0
for i,j in di:
    if(weight>=j):
        weight-=j
        pr+=i*j
    else:
        pr+=i*weight
        weight=0
    i+=1
print('%.4f'%pr)
