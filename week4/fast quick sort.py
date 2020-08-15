def swap(a,p,r,j):
    for k in range(r-p+1):
        temp=a[j+k]
        a[j+k]=a[p+k]
        a[p+k]=temp
    
def partition(a,l,r):
    p=r
    i,j=l,l
    while(i<p):
        if a[i]==a[p]:
            p=p-1
            temp=a[i]
            a[i]=a[p]
            a[p]=temp
        if a[i]<a[p]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            j+=1
        
        i+=1
    if i!=j:
        swap(a,p,r,j)
    return i,j,r-p+1
    
def quick(a,l,r):
    if l>r:
        return
    i,j,p=partition(a,l,r)

    if(i==j):
        quick(a,l,r-1)
    elif j==0:
        quick(a,l+p,r)
    else:
        quick(a,l,j-1)
        quick(a,j+p,r)
    
            
n=int(input())
a=list(map(int,input().split()))
quick(a,0,len(a)-1)
print(*a,sep=" ")
