n1=int(input())
a=list(input().split())
n2=int(input())
b=list(input().split())
ar=[[0 for i in range(n2+1)] for j in range(n1+1)]
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if a[i-1]==b[j-1]:
            ar[i][j]=1+ar[i-1][j-1]
        else:
            ar[i][j]=max(ar[i-1][j],ar[i][j-1])
print(ar[n1][n2])
