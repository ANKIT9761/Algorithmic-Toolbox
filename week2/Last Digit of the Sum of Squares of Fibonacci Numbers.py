def calc_fib(n):
    fi={0:0,1:1}
    if n in fi:
        return fi[n]
    l=[n]
    while(n>=4):
        n=int(n//2)
        l+=[n]
    a,b,j=1,1,1
    for i in range(len(l)-1,-1,-1):
        j*=2
        a,b=a*(2*b-a),a**2+b**2
        if(l[i]!=j):
            j+=1
            a,b=b,a+b
    
    return a*b
        
    
def get_length(m):
    previous=0
    current=1
    for i in range(m*m+1):
        previous,current=current,(previous+current)%m
        if(previous==0 and current==1):
            
            return i+1
def fastfib(n,m):
    rem=n%get_length(m)
    
    return calc_fib(rem)%m
    
    

n=int(input())
m=10
print(fastfib(n,m))
