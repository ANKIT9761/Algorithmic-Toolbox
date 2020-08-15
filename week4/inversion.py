def mergesort(ar,c):
    if len(ar)>1:
        m=len(ar)//2
        l=ar[:m]
        r=ar[m:]
        l,c=mergesort(l,c)
        r,c=mergesort(r,c)
    
        ar=[]

        while len(l)>0 and len(r)>0:
            if l[0]<=r[0]:
                ar.append(l[0])
                l.pop(0)
            else:
                c+=len(l)
                ar.append(r[0])
                r.pop(0)
        for i in l:
            ar.append(i)
        for i in r:
            ar.append(i)

    return ar,c
        


c=0
n=int(input())
a=list(map(int,input().split()))
a,n=mergesort(a,c)
print(n)
