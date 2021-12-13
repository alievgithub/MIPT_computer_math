'''
#A
def fib(n):
	if n <= 1:
		return n
	if F[n] == -1:
		F[n] = fib(n-1) + fib(n-2)
	return F[n]

n = int(input()) + 1
F = [-1]*(n+1)
print(fib(n))
'''
'''
#B
n = int(input())
arr = list( map(int, input().split()) )
K = [0]*n
K[0] = 1
for i in range(n-1):
	if i < n-1:
		K[i+1] += K[i]
	if i+int(arr[i]) <= n-1 and int(arr[i]) != 1:
		K[i + int(arr[i])] += K[i]
print(K[n-1]%937)
'''
'''
#C
n = int(input())
clr = list( map(int, input().split()) )
tin = list( map(int, input().split()) )
K = [0]*n
K[0] = 1
for i in range(n-1):
	if clr[i] == clr[i+1]:
		K[i+1] += K[i]
	if i < n-2:
		if clr[i] == clr[i+2]:
			K[i+2] += K[i] 
	if clr[i] != tin[i] and tin[i] != 0:
		if tin[i] == clr[i+1] :
			K[i+1] += K[i]
		if i < n-2:
			if tin[i] == clr[i+2]:
				K[i+2] += K[i]
print(K[n-1]%947)
'''
'''
#D
n = int(input())
arr = [int(input()) for i in range(n)]
K = [999999]*n
K[0] = 0
for i in range(n):
	if i < n-1:
		K[i+1] = min(K[i+1], K[i] + abs(arr[i]-arr[i+1]))
	if i < n-2:
		K[i+2] = min(K[i+2], K[i] + 3*abs(arr[i]-arr[i+2]))
print(K[n-1])
'''
