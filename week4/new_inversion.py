def bubble(a):
    c=0
    for i in range(len(a)):
        for j in range(0,len(a)-i-1):
            if(a[j]>a[j+1]):
                c+=1
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
    return c

n=int(input())
a=list(map(int,input().split()))
print(bubble(a))
