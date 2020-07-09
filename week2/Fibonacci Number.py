def fastfib(l,n):
    fib={0:0,1:1}
    a,b,i=1,1,1
    if n in fib:
        return fib[n]
    for j in range(len(l)-1,-1,-1):
        i*=2
        a,b=a*(2*b-a),a**2+b**2
        if(l[j]!=i):
            i+=1
            a,b=b,a+b
    return a

n=int(input())
l=[n]
temp=int(n)
while(temp>=4):
    l+=[int(temp/2)]
    temp//=2
print(fastfib(l,n))
