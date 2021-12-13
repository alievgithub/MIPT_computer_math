'''
#A
def merge(L, R):
    i,j = 0, 0
    n, m = len(L), len(R)
    C=[]
    while i < n and j < m:
        if L[i] < R[j]:
            C += L[i: i+1]
            i += 1
        else:
            C += R[j: j+1]
            j+=1
    C += L[i:]+R[j:]
    return C
'''
'''
#B
def merge_sort(A, depth=1, part='left'):
    print('depth:', depth, '|', 'part:', part, '|', 'array:', A)
    if len(A) < 2:
        return A
    l=merge_sort(A[:len(A)//2], depth+1, part='left')
    r=merge_sort(A[len(A)//2:], depth+1, part='right')
    A=merge(l, r)
    print('depth:', depth, '|', 'part:', part, '|', 'after merge:', A)
    return A
 
 
def merge(L, R):
    i,j = 0, 0
    n,m = len(L), len(R)
    c = []
    while i < n and j < m:
        if L[i] < R[j]:
            c += L[i:i+1]
            i += 1
        else:
            c += R[j:j+1]
            j += 1
    c += L[i:] + R[j:]
    return c
'''
'''
#C
def split_barrier(A, barrier):
    left = []
    right = []
    middle = []
    for i in A:
        if i < barrier:
            left.append(i)
        elif i > barrier:
            right.append(i)
        else:
            middle.append(i)
    for i , zhis in enumerate(left + middle + right):
        A[i] = zhis
'''
'''
#G
def selection_sort(a, s):
    if s == len(a):
        return
    n = len(a)
    k = s
    for i in range(s, n):
        if a[k] > a[i]:
            k = i
    a[s], a[k] = a[k], a[s]
    if k != s:
        print(*a)
    return selection_sort(a, s + 1)
 
 
s = input() 
a = []
for i in s.split():
    a.append(int(i))
selection_sort(a, 0)
'''
'''
#D
def hoar_sort(A, depth = 1, part = 'left'):
    print('depth:', depth, 'part:', part, 'array before:', A)
    if len(A) < 2:
        return A
    barrier = A[0]
    left, right, middle= [], [], []
    for i in A:
        if i < barrier:
            left.append(i)
        elif i > barrier:
            right.append(i)
        else:
            middle.append(i)
    x = hoar_sort(left, depth + 1, part = 'left')
    y=hoar_sort(right, depth + 1, part = 'right')
    print('depth:', depth, 'part:', part, 'array after:', x + middle + y)
    return x + middle + y
'''
'''
#E
def hoar_sort(arr, depth=1):
	if len(arr) < 2:
		return arr
	barrier = arr[0]
	left, right, middle = [], [], []
	for i in arr:
		if i < barrier:
			left.append(i)
		elif i > barrier:
			right.append(i)
		else:
			middle.append(i)
	x = hoar_sort(left, depth+1)
	y = hoar_sort(right, depth+1)
	arr = x + middle + y
	if depth == 1:
		return arr[:n//2 + 1]
	return arr
 
arr = []
n = int(input())
for i in input().split():
	arr.append(int(i))
k = 0
for i in hoar_sort(arr):
	k += i//2 + 1
print(k)
'''
'''
#F
def sort(a):
	n = len(a)
	for i in range(n - 1):
		for j in range(n - i - 1):
			if a[j] > a[j + 1]:
				a[j], a[j + 1] = a[j + 1], a[j]
 
	a = delet(a)
	return a
 
 
def delet(x):
	n = len(x)
	j = 0
	while j < n-1:
		if  x[j] == x[j + 1]:
			x.pop(j+1)
			n -= 1
		else:
			j += 1
	return x
 
 
 
n, m = input().split()
n = int(n)
m = int(m)
a = []
b = []
for i in input().split():
	a.append(int(i))
for i in input().split():
	b.append(int(i))
if n != m:
	a = sort(a)
	b = sort(b)
n = len(a)
m = len(b)
k = 0
if n != m:
	print('No')
else:
	for i in range(n):
		if a[i] != b[i]:
			k += 1
			break
	if k == 0:
		print('Yes')
	else:
		print('No')
'''
'''
#H
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        k1 = -1
        k2 = -1
        for j in range(n-i):
            if a[j] >= 0:
                s = 0
                if k1 >= 0:
                    if a[j] < a[k1]:
                        s += 1
                        sort(j, k1)
                if j < n-1-i:
                    if a[j+1] >= 0 and s == 0:
                        if a[j] > a[j+1]:
                            sort(j, j+1)
                    else:
                        k1 = j
            else:
                s = 0
                if k2 >= 0:
                    if a[j] > a[k2]:
                        s += 1
                        sort(j, k2)
                if j < n-i-1:
                    if a[j+1] < 0 and s == 0:
                        if a[j] < a[j+1]:
                            sort(j, j+1)
                    else:
                        k2 = j
 
def sort(i, j):
    a[j], a[i] = a[i], a[j]
    print(*a)
 
 
s = input()
s = s.split()
a = list(map(int, s))
bubble_sort(a)
'''
