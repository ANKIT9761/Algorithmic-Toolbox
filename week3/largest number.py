def largestNumber(array): 
      
 
    extval, ans = [], "" 
      

    l = len(str(max(array))) + 1
      

    for i in array: 
        temp = str(i) * l
          

        extval.append((temp[:l:], i)) 
      
    
    extval.sort(reverse = True) 
      
    
    for i in extval: 
          
        ans += str(i[1]) 
  
    if int(ans)==0: 
        return "0"
    return ans 
  
n=int(input())
a = list(map(int,input().split()))
  
print(largestNumber(a)) 
