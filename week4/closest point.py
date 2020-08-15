
import math 


class Point(): 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 


def dist(p1, p2): 
	return math.sqrt((p1.x - p2.x) *
					(p1.x - p2.x) +
					(p1.y - p2.y) *
					(p1.y - p2.y)) 


def bruteForce(P, n): 
	min_val = float('inf') 
	for i in range(n): 
		for j in range(i + 1, n): 
			if dist(P[i], P[j]) < min_val: 
				min_val = dist(P[i], P[j]) 

	return min_val 


def stripClosest(strip, size, d): 
	

	min_val = d 

	strip.sort(key = lambda point: point.y) 

	for i in range(size): 
		j = i + 1
		while j < size and (strip[j].y -
							strip[i].y) < min_val: 
			min_val = dist(strip[i], strip[j]) 
			j += 1

	return min_val 


def closestUtil(P, n): 

	if n <= 3: 
		return bruteForce(P, n) 

	
	mid = n // 2
	midPoint = P[mid] 

	dl = closestUtil(P[:mid], mid) 
	dr = closestUtil(P[mid:], n - mid) 

	d = min(dl, dr) 


	strip = [] 
	for i in range(n): 
		if abs(P[i].x - midPoint.x) < d: 
			strip.append(P[i]) 

	
	return min(d, stripClosest(strip, len(strip), d)) 
 
def closest(P, n): 
	P.sort(key = lambda point: point.x) 

	return closestUtil(P, n) 


n=int(input())
P=[]
for i in range(n):
    s=list(map(int,input().split()))
    P.append(Point(s[0],s[1]))
n = len(P) 
print(closest(P, n))  
