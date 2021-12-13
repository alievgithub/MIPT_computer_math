'''
#A
line = input()
arr = []
i = l = k = 0
for x in line.split():
	x = int(x)
	arr.append(x)
	i += 1
n = i
r = -1
while l < n:
	r += 1
	minimum = arr[r]
	old = r
	while r < n:
		if arr[r] < minimum:
			minimum = arr[r]
			k = r
			change = 1
		r += 1
	if k != l and change == 1:
		arr[k] = arr[l]
		arr[l] = minimum
		i = 0
		while i < n:
			print(arr[i], end = " ")
			i += 1
		print()
	r = old
	change = 0
	l += 1
'''
'''
#B
def insert_sort(arr):
	N = len(arr)
	for top in range(1, N):
		k = top
		while k > 0 and arr[k - 1] > arr[k]:
			arr[k], arr[k - 1] = arr[k - 1], arr[k]
			k -= 1
			for i in range(N):
				print(arr[i], end = " ")
			print()
	if k > 0:
		return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if insert_sort(arr) == 1:
	for i in range(N):
		print(arr[i], end = " ")
	print()
'''
'''
#C
def fool_sort(arr):
	i = 0
	N = len(arr)
	while i < len(arr) - 1:
		if arr[i] > arr[i + 1]:
			arr[i], arr[i + 1] = arr[i + 1], arr[i]
			i=0
			for j in range(N):
				print(arr[j], end = " ")
			print()
			k=1
		else:
			i += 1
			k=0
	if k == 1:
		return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if fool_sort(arr) == 1:
	for j in range(N):
		print(arr[j], end = " ")
	print()
'''
'''
#D
def bubble_sort(arr):
	i = 0
	N = len(arr)
	for bypass in range(1, N):
		for k in range(0, N - bypass):
				if arr[k] > arr[k + 1]:
					arr[k], arr[k + 1] = arr[k + 1], arr[k]
					for j in range(N):
						print(arr[j], end = " ")
					print()
	return 1

line = input()
arr = []
N = 0
for x in line.split():
	x = int(x)
	arr.append(x)
if bubble_sort(arr) == 1:
	for j in range(N):
		print(arr[j], end = " ")
	print()
'''
'''
#E
line = input()
arr = []
M = 0
for x in line.split():
	x = int(x)
	arr.append(x)
count = [0] * 10
for i in arr:
		count[i] += 1
		for j in range(10):
			print(count[j], end = ' ')
		print()
for i in range(10):
	if count[i]>0:
		print((str(i) + ' ') * count[i], end = '')
'''
'''
#F
line = input()
arr = []
for x in line.split():
	x = int(x)
	arr.append(x)
N = len(arr)
length = len(str(max(arr)))
rang = 2
for i in range(length):
	zero = [[] for k in range(rang)]
	for x in arr:
		figure = x // 10**i % 2
		zero[figure].append(x)
	arr = []
	for k in range(rang):
		arr = arr + zero[k]
	for l in range(N):
		print(arr[l], end = " ")
	print()
'''
'''
#G
tot = N = 0
n = int(input())
arr = []
count = []
for i in range(n):
	x = int(input())
	arr.append(x)
	while x > 0:
		tot += x % 10
		x //= 10
	count.append(tot)
	tot = 0
r = -1
def insert_sort(arr):
	N = len(arr)
	for top in range(1, N):
		k = top
		while k > 0 and count[k - 1] >= count[k]:
			count[k], count[k - 1] = count[k - 1], count[k]
			if count[k - 1] == count[k]:
				if  arr[k - 1] > arr[k]: 
					arr[k - 1], arr[k] = arr[k], arr[k - 1]
			else:
				arr[k], arr[k - 1] = arr[k - 1], arr[k]
			k -= 1
	for i in range(N):
		print(arr[i])
	return 1
	

if insert_sort(arr) == 1:
	for i in range(N):
		print(arr[i])
'''
'''
#H
n = int(input())
arr = []
even = []
num = []
for i in range(n):	arr.append(int(input()))
for i in range(len(arr)):
	if arr[i] % 2 == 0:
		num.append(i)
		even.append(arr[i])
for j in range(len(even) * 2):
	for i in range(len(even) - 1):
		if even[i + 1] < even[i]:
			even[i], even[i + 1] = even[i + 1], even[i]
k = 0
for i in num:
	arr[i] = even[k]
	k += 1
for i in range(len(arr)):
	print(arr[i], end = ' ')
print()
'''
