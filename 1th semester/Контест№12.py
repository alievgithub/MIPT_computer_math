'''
#A
y, x = input().split()
x = int(x)
y = int(y)
lst = [[0] * 10 for i in range(9)]
lst[x][y] = 1
for i in range(x+1, 9):
	for j in range (1, 9):
		lst[i][j] = lst[i-1][j-1] + lst[i-1][j+1]

print(sum(lst[8]))
'''
'''
#D
a = input()
b = input()
lst = [[(i+j) if i*j == 0 else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
for i in range(1, len(a)+1):
	for j in range(1, len(b)+1):
		if a[i-1] == b[j-1]:
			lst[i][j] = lst[i-1][j-1]
		else:
			lst[i][j] = 1 + min(lst[i-1][j-1], lst[i-1][j], lst[i][j-1])
print(lst[len(a)][len(b)])
'''
'''
#B
n, m = int(input()), int(input())
lst = [[0]*m for _ in range(n)]
for i in range(n):
	for j in range(m):
		lst[i][j] = int(input())

for i in range(m-2, -1, -1):
	lst[-1][i] += lst[-1][i+1]
for j in range(n-2, -1, -1):
	lst[j][-1] += lst[j+1][-1]
for j in range(n-2, -1, -1):
	for i in range(m-2, -1, -1):
		lst[j][i] += min(lst[j+1][i], lst[j][i+1])

coin = int(input())
frac = coin - lst[0][0]
if frac < 0:
	print("Impossible")
else:
	print(frac)
'''
'''
#C
def c(x, y):
	if (str(x)+str(y+1) not in black):
		return True
	else:
		return False
def l(x, y):
	if (str(x-1)+str(y+1) in black):
		return True
	else:
		return False
def r(x, y):
	if (str(x+1)+str(y+1) in black):
		return True
	else:
		return False
def sp(x, y, N):
	if y == 8:
		return N
	if x == 1:
		if c(x, y) and r(x, y):
			return sp(x, y+1, N) + sp(x+1, y+1, N)
		elif c(x, y):
			return sp(x, y+1, N)
		elif r(x, y):
			return sp(x+1, y+1, N)
		else:
			return 0
	if x == 8:
		if c(x, y) and l(x, y):
			return sp(x, y+1, N) + sp(x-1, y+1, N)
		elif c(x, y):
			return sp(x, y+1, N)
		elif l(x, y):
			return sp(x-1, y+1, N)
		else:
			return 0
	if 2<=x<=7:
		if c(x, y) and l(x, y) and r(x, y):
			return sp(x, y+1, N) + sp(x-1, y+1, N)  + sp(x+1, y+1, N)
		elif c(x, y) and l(x, y):
			return sp(x, y+1, N) + sp(x-1, y+1, N)
		elif c(x, y) and r(x, y):
			return sp(x, y+1, N) + sp(x+1, y+1, N)
		elif l(x, y) and r(x, y):
			return sp(x-1, y+1, N) + sp(x+1, y+1, N)
		elif l(x, y):
			return sp(x-1, y+1, N)
		elif c(x, y):
			return sp(x, y+1, N)
		elif r(x, y):
			return sp(x+1, y+1, N)
		else:
			return 0
n = int(input())
black = []
xdict =	{
	"a": 1,
	"b": 2,
	"c": 3,
	"d": 4,
	"e": 5,
	"f": 6,
	"g": 7,
	"h": 8,
}
for i in range(n):
	temp = input()
	black.append(str(xdict[temp[0]])+str(temp[1]))
white = input()
wx = xdict[white[0]]
wy = int(white[1])
print(sp(wx, wy, 1))
'''
'''
#E
def lcs(s1, s2):
	a = len(s1)
	b = len(s2)
	s_matrix = [[0 for i in range(b+1)] for i in range(a+1)]
	for i in range(1, a+1):
		for j in range(1, b+1):
			if i == 0 or j == 0:
				s_matrix[i][j] = 0
			elif s1[i-1] == s2[j-1]:
				s_matrix[i][j] = 1 + s_matrix[i-1][j-1]
			else:
				s_matrix[i][j] = max(s_matrix[i-1][j], s_matrix[i][j-1])
	index = s_matrix[a][b]
	result = [""] * index
	i = a
	j = b
	while i > 0 and j > 0:
		if s1[i-1] == s2[j-1]:
			result[index-1] = s1[i-1]
			i -= 1
			j -= 1
			index -= 1
		elif s_matrix[i-1][j] > s_matrix[i][j-1]:
			i -= 1
		else:
			j -= 1
	return result
'''
'''
#F
from bisect import bisect_left, bisect_right
from functools import cmp_to_key

def lis(s, mode='strictly', order='increasing', key=None, index=False):
	bisect = bisect_left if mode.startswith('strict') else bisect_right
	rank = s if key is None else map(key, s)
	if order == 'decreasing':
		rank = map(cmp_to_key(lambda x,y: 1 if x<y else 0 if x==y else -1), rank)
	rank = list(rank)
	if not rank: return []
	last = [0]
	predecessor = [None]
	for i in range(1, len(s)):
		j = bisect([rank[k] for k in last], rank[i])
		try: last[j] = i
		except: last.append(i)
		predecessor.append(last[j-1] if j > 0 else None)
	def trace(i):
		if i is not None:
			yield from trace(predecessor[i])
			yield i
	indices = trace(last[-1])
	return list(indices) if index else [s[i] for i in indices]
'''
