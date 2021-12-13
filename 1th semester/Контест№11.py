'''
#A
k = 0
sent = []
sent = input().split()

for j in range(len(sent)):
	for i in range(len(sent)):
		if len(sent[i]) < 5:
			del sent[i]
			break

for x in sent:
	count = 0
	for y in x: count += ord(y)
	sent[k] = count
	k += 1
print(*sent)
'''
'''
#B
k = 0
sent = []
sent = input().split()

list.sort(sent, key = len)
for i in range(1, len(sent)):
	if len(sent[i]) == len(sent[i-1]) and sent[i] < sent[i-1]:
		sent[i-1], sent[i] = sent[i], sent[i-1]

for x in sent:
	count = 0
	for y in x: count += ord(y)
	sent[k] = count
	k += 1
print(*sent)
'''
'''
#C
def prefix(n):
	p = [0] * len(n)
	for i in range(1, len(n)):
		k = p[i - 1]
		while k > 0 and n[k] != n[i]:
			k = p[k - 1]
		if n[k] == n[i]:
			k += 1
			p[i] = k
	return p

print(*prefix(input()))
'''
'''
#D
def z_func(n):
	n += '#'
	l, r = 0, 0
	z = [0] * len(n)
	for i in range(1, len(n)):
		z[i] = max(0, min(z[i - l], r - i))
		while n[z[i]] == n[i + z[i]]:
			z[i] += 1
		if i + z[i] > r:
			l, r = i, i + z[i]
	return z[:-1]

print(*z_func(input()))
'''
'''
#E
def KMP(word, template):
	pattern = list(template)
	shifts = [1] * (len(template) + 1)
	shift = 1
	for pos in range(len(template)):
		while shift <= pos and template[pos] != template[pos-shift]:
			shift += shifts[pos-shift]
		shifts[pos+1] = shift
	start = 0
	match = 0
	for c in word:
		while match == len(template) or \
		match >= 0 and template[match] != c:
			start += shifts[match]
			match -= shifts[match]
		match += 1
		if match == len(template):
			yield start
t = input()
w = input()
out = []
for i in KMP(w, t):
	out.append(i)
if out == []:
	out.append(-1)
print(*out)
'''
'''
#F
def A(s):
	s += '#'
	l, r = 0, 0
	z = [0] * len(s)
	for i in range(1, len(s)):
		z[i] = max(0, min(z[i - l], r - i))
		while s[z[i]] == s[i + z[i]]:
			z[i] += 1
		if i + z[i] > r:
			l, r = i, i + z[i]
	return z[:-1]
Str = input()
L = len(Str)
StrA = Str[::-1]
Str += StrA
sol = A(Str)

i = len(sol) - 1
while(i >= L):
    print(sol[i], end=' ')
    i -= 1
'''
'''
#G
#Превышено время работы
a, b = input(), input()
x, y = 0, 0
for i in range(len(a)):
	if a == b:
		y = 1
		break
	a = a[1:] + a[0]
	x += 1
x = -1 if y == 0 else x
print(x)
'''
