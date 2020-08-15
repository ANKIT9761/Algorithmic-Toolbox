n1,n2=map(int,input().split())
a=[]
c=0
for i in range(n1):
    x,y=map(int,input().split())
    a.append((x,"l"))
    a.append((y,"r"))
p=list(map(int,input().split()))
for i in p:
    a.append((i,"p"))
a.sort()
b={}
for i in a:
    if i[1]=='l':
        c+=1
    elif i[1]=='r':
        c-=1
    elif i[1]=='p':
        b[i[0]]=c
for i in p:
    print(b[i],end=" ")

