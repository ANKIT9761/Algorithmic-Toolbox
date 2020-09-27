n=int(input())
l=list(map(int,input().split()))
if sum(l)%3!=0:
    print(0)
else:
    ma=[[0 for i in range(sum(l)//3+1)] for i in range(len(l)+1)]
    
    count=0
    for i in range(len(l)+1):
        ma[i][0]=1
    for i in range(1,len(l)+1):
        for s in range(sum(l)//3+1):
            if s>=l[i-1]:
                ma[i][s]=ma[i-1][s] or ma[i-1][s-l[i-1]]
            else:
                ma[i][s]=ma[i-1][s]
    
    for i in range(1,len(l)+1):
        if ma[i][-1]==1:
            count+=1
    if count>=3:
        print(1)
    else:
        print(0)
        

        
