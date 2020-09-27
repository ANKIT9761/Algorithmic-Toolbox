s=input()
op=[]
nu=[]
for i in s:
    if i.isdigit():
        nu.append(int(i))
    else:
        op.append(i)
ma=[[0 for j in range(len(nu))] for i in range(len(nu))]
mi=[[0 for j in range(len(nu))] for i in range(len(nu))]

for i in range(len(nu)):
    ma[i][i]=nu[i]
    mi[i][i]=nu[i]
    
def findmaxmin(i,j):
    mim=+1000000000
    mam=-1000000000
    for k in range(i,j):
        a=calc(ma[i][k],ma[k+1][j],op[k])
        b=calc(ma[i][k],mi[k+1][j],op[k])
        c=calc(mi[i][k],mi[k+1][j],op[k])
        d=calc(mi[i][k],ma[k+1][j],op[k])
        mim=min(mim,a,b,c,d)
        mam=max(mam,a,b,c,d)
    return (mim,mam)
    
    
def calc(a,b,op):
    if op=='+':
        return a+b
    elif op=='-':
        return a-b
    elif op=='*':
        return a*b
    elif op=='/':
        return a/b
for s in range(1,len(nu)):
    for i in range(0,len(nu)-s):
        j=i+s
        mi[i][j],ma[i][j]=findmaxmin(i,j)
print(ma[0][len(nu)-1])
    
