n1=int(input())
a=list(map(int,input().split()))
n2=int(input())
b=list(map(int,input().split()))
n3=int(input())
c=list(map(int,input().split()))
ar=[[[0 for k in range(n3+1)] for j in range(n2+1)] for i in range(n1+1)]

for i in range(1,n1+1):
    for j in range(1,n2+1):
        for k in range(1,n3+1):
            if a[i-1]==b[j-1]==c[k-1]:
                ar[i][j][k]=ar[i-1][j-1][k-1]+1
            else:
                ar[i][j][k]=max(ar[i-1][j][k],ar[i][j-1][k],ar[i][j][k-1])
print(ar[n1][n2][n3])
