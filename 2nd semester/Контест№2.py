'''
#A
def poly_hash(p, m ,s):
    h = 0
    n = len(s)
    for i in range(n):
        h += ord(s[i])*(p**(n-i-1))
    h = h%m
    return h

p, m = input().split()
s = input()
p = int(p)
m = int(m)
print(poly_hash(p, m, s))
'''
'''
#B
def poly_hash(p, m ,s):
    h = 0
    n = len(s)
    for i in range(n):
        h += ord(s[i])*(p**(n-i-1))
    h = h%m
    return h

def insert(table, key, value):
    hash = poly_hash(91, 100, key)
    chain = table[hash % s_table]
    for e in chain:
        e_hash, e_key, e_value = e
        if hash == e_hash:
            if key == e_key:
                e[2] = value
                return
    chain.append([hash, key, value])

s_table = 10
s_hash = 91
s_mod = 100
table = [[] for i in range(s_table)]
k = int(input())
for i in range(k):
    key, value = input().split()
    insert(table, key, value)
for i in range(len(table)):
    if table[i]:
        print(i)
        for j in table[i]:
            print(' '.join(map(str, j)))
'''
'''
#C
def poly_hash(s):
    h = 0
    for c in s:
        h = ((h*p) + ord(c)) % m
    return h

p = 91
m = 100

def search(table, key):
    k = 0
    for p in range(10):
        for e in table[p]:
            if e[0] == poly_hash(key):
                if e[1] == key:
                    k = 1
            if k == 1:
                return e[2]
    else:
        return 'KeyError'
'''
'''
#D
def poly_hash(s):
    h = 0
    for c in s:
        h = ((h*p) + ord(c)) % m
    return h

p = 91
m = 100

def remove(table, key):
    k = 0
    for p in range(10):
        for e in table[p]:
            if e[0] == poly_hash(key):
                if e[1] == key:
                    k = 1
            if k == 1:
                table[p].remove(e)
                return e[2]
    else:
        return 'KeyError'
'''
'''
#E
b = 37
M = (1 << 64) - 1
def code(c):
    return ord(c) - ord("a") + 1

def polyhash(s):
    h = [0]
    for c in s:
        h.append(((h[-1]*b) + code(c)) % M)
    return h

t = input()
s = input()
n = len(t)
m = len(s)
s = polyhash(s)
t = polyhash(t)[-1]
l = []
k = 0
f = b**n%M
for i in range(m - n + 1):
    if t == (s[i+n] - (s[i]*f)) % M:
        l.append(i)
        k = 1
if k == 1:
    print(" ".join(map(str,l)))
else:
    print(-1)
'''
