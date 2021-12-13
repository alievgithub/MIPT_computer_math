'''
#A
N = int(input())
K = int(input())
list = input()
i = tst = 0
for x in list.split():
	i += 1
	if int(x) == K:
		tst = 1
		break
if tst == 1:
	print(i)
else:
	print(-1)
'''
'''
#B
#Не рабочий вариант
def find(n):
	if arr[n] == K:
		return n + 1
	elif n < 1:
		return -1
	else:
		return find(n-1)

arr = list( map(int, input().split()) )
K = int(input())
n = len(arr) - 1
print(find(n))
'''
'''
#B
def find(arr, left, right):
	global x
	if left == right-1:
		return -1
	m = (left+right) // 2
	if int(arr[m]) < x:
		return find(arr, m, right)
	elif int(arr[m]) == x:
		return m+1
	else:
		return find(arr, left, m)

arr = []
arr = input().split()
x = int(input())
n = len(arr)
left = -1
right = len(arr)
print(find(arr, left, right))
'''
'''
#D
N = int(input())
arr = list( map(int, input().split()) )
for i in range(N-1):
    for j in range(N-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
Shrek = croupier = 0
for i in range (N):
	if i < N//2:
		croupier += arr[i]
	else:
		Shrek += arr[i]
print(Shrek - croupier)
'''
'''
#C
def find_root(f, a, b, tol):
	eps = 1e-6
	while b - a > tol and b - a >= eps:
		x = (a + b)/2
		if f(x) == 0:
			break
		y = f(x)
		g = f(a)
		if y*g > 0:
			a = x
		else:
			b = x
	return x
'''
'''
#E
def viv(matrix, N):
	for z in range(N):
		print(*matrix[z])
	print()
def bubble_sort2d(matrix, N, M):
	viv(matrix, N)
	for g in range(N*M):
		for i in range(N):
			for j in range(M-1):
				if i>0 and j==0:
					if matrix[i-1][M-1] > matrix[i][j]:
						matrix[i-1][M-1], matrix[i][j] = matrix[i][j], matrix[i-1][M-1]
						viv(matrix, N)
				if matrix[i][j] > matrix[i][j+1]:
					matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
					viv(matrix, N)
'''
'''
#G
x = []
y = []
point = []
name = []
quan = 0
rooms = int(input())
for i in range(rooms):
	players = int(input())
	quan += players
	for j in range(players):
		x, y = input().split()
		point.append(float(x))
		name.append(y)
for i in range(len(point)-1):
        k=i
        for j in range(i+1, len(point)):
            if point[k] < point[j]:
                k = j
        point[i], point[k] = point[k], point[i]
        name[i], name[k] = name[k], name[i]
print(quan)
for f in range(len(point)):
	print('%.2f' % point[f], name[f])
'''
