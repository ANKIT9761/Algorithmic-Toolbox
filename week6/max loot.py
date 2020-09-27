w,n=list(map(int,input().split()))
l=list(map(int,input().split()))

ma=[[0 for j in range(w+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,w+1):
        val=ma[i-1][j]
        if j>=l[i-1]:
            v=ma[i-1][j-l[i-1]]+l[i-1]
            if v>val:
                val=v
        ma[i][j]=val
print(ma[n][w])
            
            
