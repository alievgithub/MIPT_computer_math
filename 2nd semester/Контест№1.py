'''
#A
x = -1
max = x
while x != 0:
	x = int(input())
	if x > max:
		max = x
		count = 0
	if x == max:
		count += 1
print(count)
'''
'''
#B
def dot_product(N, vector1, vector2):
	comp = 0
	for i in range(N):
		comp += vector1[i]*vector2[i]
	return(comp)
'''
'''
#C
def F(n):
	if n == 0:
		return(1)
	else:
		return(n - M(F(n-1)))

def M(n):
	if n == 0:
		return(0)
	else:
		return(n - F(M(n-1)))
'''
'''
#D
n = int(input())
x = y = 0
num = -2
arr = []
for i in input().split():
	i = int(i)
	z = y
	y = x
	x = i
	num += 1
	if num > 0 and ((y > z and y > x) or (y < z and y < x)):
		arr.append(num)
print(*arr)
'''
'''
#F
n = int(input())
arr = [int(input()) for i in range(n)]
arr_ans =[999999 for i in range(n)]
arr_ans[0] = 0
for i in range(n):
	if i < n - 1:
		arr_ans[i+1] = min(arr_ans[i+1], arr_ans[i] + abs(arr[i] - arr[i+1]))
	if i < n - 2:
		arr_ans[i+2] = min(arr_ans[i+2], arr_ans[i] + 3*abs(arr[i] - arr[i+2]))
print(arr_ans[n-1])
'''
'''
#Eshka
N = int(input())
a = [0] * N
a0 = [[0] * N for i in range(N)]
for i in range(N):
	line = input().split()
	a[i] = line
for i in range(N):
	for j in range(N):
		a0[i][j] = a[i][j]
for i in range(N):
	for j in range(N):
		a[i][j] = a0[j][i]
for i in range(N):
	for j in range(N):
		print(a[i][j], end = " ")
	print()
'''
'''
#G
n = int(input())
a, d, m, y, t, t1, t2, a1 = [0]*n, [0]*n, [0]*n, [0]*n, [0]*n, [0]*n, [0]*n, [0]*n
dict = {'January' : 1, 'February' : 2, 'March' : 3, 'April' : 4, 'May' : 5, 'June' : 6, 'July' : 7, 'August' : 8, 'September' : 9, 'October' : 10, 'November' : 11, 'December' : 12}
def bubble_sort(a):
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a
for i in range(n):
    d[i], m[i], y[i], t[i] = input().split()
    t1[i], t2[i] = t[i].split(':')
    a[i] = int(y[i])*(10**8) + int(dict[m[i]])*(10**6) + int(d[i])*(10**4) + int(t1[i])*(10**2) + int(t2[i])
    a1[i] = a[i]
a = bubble_sort(a)
for i in range(n):
    for j in range(n):
        if a[i] == a1[j]:
            print(d[j], m[j], y[j], t[j], sep=" ")
            break
'''
