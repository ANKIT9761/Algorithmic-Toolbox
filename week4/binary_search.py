# Uses python3
import sys

def binary_search(a,l,r,x):
    mid=(l+r)//2
    if l<r:
        if x==a[mid]:
            print(mid,end=" ")
        elif(x<a[mid]):
            binary_search(a,l,mid-1,x)
        elif(x>a[mid]):
            binary_search(a,mid+1,r,x)
    else:
        if l==r and x==a[l]:
            print(l,end=" ")
        else:
            print(-1,end=" ")
        

n1,*a=list(map(int,input().split()))
n2,*b=list(map(int,input().split()))
for i in b:
    l,r=0,n1-1
    binary_search(a,l,r,i)
        


