d=int(input())
capacity=int(input())
n=int(input())
arr=[0]+list(map(int,input().split()))+[d]
current_refill=0
count=0

while current_refill<=n:
    last_refill=current_refill
    while(current_refill<=n and arr[current_refill+1]-arr[last_refill]<=capacity):
        current_refill+=1
    if current_refill==last_refill:
        count=-1
        break
    if current_refill<=n:
        count+=1
print(count)
