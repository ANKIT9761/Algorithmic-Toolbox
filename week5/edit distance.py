a=input()
b=input()
n,m=len(a),len(b)
matrix=[]
for i in range(n+1):
    l=[]
    for j in range(m+1):
        
        if i==0:
            l.append(j)
        else:
            if j==0:
                l.append(i)
            else:
                l.append(0)
    matrix.append(l)

for i in range(1,n+1):
    for j in range(1,m+1):
        m1=matrix[i-1][j]+1
        m2=matrix[i][j-1]+1
        m3=matrix[i-1][j-1]
        m4=matrix[i-1][j-1]+1
        
        if a[i-1]==b[j-1]:
            matrix[i][j]=min(m1,m2,m3)
        else:
            matrix[i][j]=min(m1,m2,m4)
        
print(matrix[n][m])
