'''
#A
def cycle_shift(arr, N):
	arr.append(arr[0])
	arr.pop(0)
'''
'''
#B
n=int(input())
arr=[]
for i in range(n):
	a=int(input())
	arr.append(a)
arr.reverse()
for i in range(n):
	print(arr[i])
'''
'''
#C
n=int(input())
arr=[]
tst=0
for i in range(n):
	a=int(input())
	arr.append(a)
div=int(input())
for i in range(n):
	a=arr[i]
	if a%div==0:
		print(i, end=' ')
		tst=1
if tst==0:
	print(-1)
'''
'''
#D
first=second=third=0
i=-2
n=int(input())
line=input()
for x in line.split():
     i+=1
     x=int(x)
     first=second
     second=third
     third=x
     if ((first<second and third<second) or (first>second and third>second)) and i!=0:
         print(i, end=' ')
'''
'''
#E
n=int(input())
line=input().split()
for i in range(len(line)):
	if line[i:]==line[i:][::-1]:
		print(i)
		if(i!=0):
			print(*line[:i][::-1])
		break
'''
'''
#F
n=int(input())
l=[]
r=[]
c=[]
for i in range(n):
	l.append(int(input()))
	r.append(int(input()))
	c.append(int(input()))
M=int(input())
arr=[]
for i in range(M):
	arr.append(0)
for j in range(M):
	ind=int(input())
	for i in range(n):
		if l[i]<=ind and ind<=r[i]:
			arr[j]=c[i]
for i in range(M):
	print(arr[i], end=' ')
'''
'''
#I
n=int(input())
arr=[]
hm_dist=0
localdist=100000000000000000
arr=list(map(int, input().split()))
house_ind=[]
shop_ind=[]
for i in range(n):
	if arr[i]==1:
		house_ind.append(i)
	if arr[i]==2:
		shop_ind.append(i)
for i in range(len(house_ind)):
	for j in range(len(shop_ind)):
		dist=abs(house_ind[i]-shop_ind[j])
		if dist<localdist:
			localdist=dist
	if localdist>hm_dist:
		hm_dist=localdist
	localdist=100000000000000000
print(hm_dist)
'''
'''
#H
def largest_rect(N, A):
	ans=0
	A=[-1]+A
	A.append(-1)
	N=len(A)
	stack=[0]
	for i in range(N):
		while A[i]<A[stack[-1]]:
			h=A[stack.pop()]
			area=h*(i-stack[-1]-1)
			ans=max(ans, area)
		stack.append(i)
	return ans
'''
'''
#G
N=int(input()) 
M=int(input()) 
post=[["0"]*M for i in range(N)] 
K=int(input()) 
for i in range(K): 
	x=int(input())-1 
	y=int(input())-1 
	post[x][y]=-1 
for i in range(N): 
	for j in range(M): 
		if post[i][j]!=-1: 
			cnt=0 
			for k in range(i-1, i+2): 
				for l in range(j-1, j+2): 
					if k>=0 and k<N and l>=0 and l<M: 
						if post[k][l]==-1: 
							cnt+=1 
			if cnt>0: 
				post[i][j]=cnt 

for i in range(N): 
	for j in range(M): 
		print(post[i][j], end=' ') 
	print()
'''
'''
#J
a, b=map(int, input().split()) 
c=[] 
for i in range(a): 
	Temp=input() 
	TempArr=[] 
	for j in range(len(Temp)): 
		TempArr.append(ord(Temp[j])) 
	if len(TempArr)<b: 
		TempArr+=[ord(" ")]*(b-len(Temp)) 
	c.append(TempArr) 
for i in range(a): 
	for j in range(b): 
		if c[i][j]==32: 
			c[i][j]=0 
		if c[i][j]==35: 
			c[i][j]=1 
		if c[i][j]==64: 
			c[i][j]=2 
def func(c):
	while True: 
		count=0 
		for i in range(a): 
			for j in range(b): 
				if c[i][j]==2: 
					count=1 
					if i==0 or i==a-1 or j==0 or j==b-1: 
						return(1) 
					if c[i-1][j]==0: 
						c[i-1][j]=2 
					if c[i+1][j]==0: 
						c[i+1][j]=2 
					if c[i][j-1]==0: 
						c[i][j-1]=2 
					if c[i][j+1]==0: 
						c[i][j+1]=2 
					c[i][j]=1 
		if count==0:
			break 
	if count==0: 
		return(0)
if func(c)==1: 
	print("YES") 
else: 
	print("NO")
'''
