def op(n):
    seq=[0 for i in range(n+1)]
    for i in range(2,n+1):
        m1=seq[i-1]
        m2=10000000
        m3=10000000
        if i%3==0:
            m2=seq[int(i//3)]
        if i%2==0:
            m3=seq[int(i//2)]
        seq[i]=min(m1,m2,m3)+1
    return seq
def gen_series(n,l):
    seq=[]
    while n>0:
        seq.append(n)
        if n%3!=0 and n%2!=0:
            n-=1
        elif n%3==0 and n%2==0:
            n=n//3
        elif n%2==0:
            if l[n-1]<l[int(n//2)]:
                n-=1
            else:
                n=n//2
        elif n%3==0:
            if l[n-1]<l[int(n//3)]:
                n-=1
            else:
                n=n//3
        n=int(n)
    return seq
        
            
def calc(n):
    
    if n==1:
        return [1]
    op_li=op(n)

    return gen_series(n,op_li)

n=int(input())
s=calc(n)
print(len(s)-1)
print(*s)
