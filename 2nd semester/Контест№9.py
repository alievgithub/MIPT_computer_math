'''
#A
from collections import deque
def main():
    n, m, v1, v2 = input().split()
    m = int(m)
    start = v1
    finish = v2
    g = read_graph(m)
    s = dijkstra(g, start)
    c = []
    c.append(finish)
    shortest_path = reveal_shortest_path(g, start, finish, s, c)
    shortest_path[:] = shortest_path[::-1]
    print(*shortest_path)
def read_graph(m):
    g = {}
    for i in range(m):
        a, b, weight = input().split()
        weight = int(weight)
        add_edge(g, a, b, weight)
        add_edge(g, b, a, weight)
    return g
def add_edge(g, a, b, weight):
    if a not in g:
        g[a] = {b:weight}
    else:
        g[a][b] = weight
def dijkstra(g, start):
    q = deque()
    s = {}
    s[start] = 0
    q.append(start)
    while q:
        v = q.pop()
        for u in g[v]:
            if u not in s or s[v] + g[u][v] < s[u]:
                s[u] = s[v] + g[v][u]
                q.append(u)
    return s
def reveal_shortest_path(g, start, finish, s, c):
    for x in g[finish]:
        if g[x][finish] + s[x] == s[finish]:
            c.append(x)
            reveal_shortest_path(g, start, x, s, c)
    return c
main()
'''
'''
#B
n, m ,s = map(int, input().split())
e = []
g = {i: [] for i in range(n)}
for _ in range(m):
    v1, v2, w = map(int, input().split())
    arr = (v1, v2, w)
    e.append(arr)
    g[v1].append((v2, w))

def dfs(a):
    d[a] = "UDF"
    for b, _ in g[a]:
        if d[b] != "UDF":
            dfs(b)

d = [float("inf")] * n
d[s] = 0
p = [-1] * n
fix = None
for i in range(n):
    for v1, v2, w in e:
        if d[v2] > d[v1] + w:
            d[v2] = d[v1] + w
            p[v2] = v1
            if i == n - 1:
                fix = v2
                break

if fix is not None:
    for _ in range(n):
        fix = p[fix]
    dfs(fix)

for i in range(n):
    if d[i] == float("inf"):
        d[i] = "UDF"
print(" ".join(map(str, d)))
'''
'''
#C
from collections import deque

n, m = map(int, input().split())
g = [[-1 for _ in range(n)] for _ in range(n)]
for i in range(m):
    v1, v2, w = map(int, input().split())
    g[v1][v2] = w
    g[v2][v1] = w

def sum(a, arr):
    d = [float("inf")] * n
    d[a] = 0
    queue = deque([a])
    while queue:
        u = queue.popleft()
        for i in range(n):
            if arr[u][i] != -1:
                k = g[u][i]
                if d[i] > d[u] + arr[u][i]:
                    queue.append(i)
                    d[i] = d[u] + k
    sum = 0
    for i in range(n):
        if d[i] != float("inf"):
            sum += d[i]
    return sum

c = -1
s = 0
for i in range(n):
    if c == -1 or sum(i, g) < s:
        s = sum(i, g)
        c = i
print(c)
'''
'''
#E
c = list(map(int, input().split()))
q = float("inf")
def up(h, i):
    while i > 0 and d[h[(i-1)//2]] > d[h[i]]:
        r[h[i]], r[h[(i-1)//2]] = (i-1)//2, i
        h[i], h[(i-1)//2] = h[(i-1)//2], h[i]
        i = (i-1)//2
def down(h, i):
    n = len(h)
    while i*2 +1 < n:
        j = i
        if (d[h[i]] > d[h[i*2+1]]):
            j = i*2 + 1
        if i*2 + 2 < n and d[h[j]] > d[h[i*2+2]]:
            j = i*2+2
        if i == j:
            break
        r[h[i]], r[h[j]] = j, i
        h[i], h[j] = h[j], h[i]
        i = j

def minimum(h):
    x = h[0]
    h[0] = h.pop()
    r[h[0]] = 0
    down(h, 0)
    return x
n = c.pop(0)
m = c.pop(0)
r = [0]*n
g = [[] for i in range(n)]
h = [i for i in c] + [i for i in range(n) if i not in c]
for e in range(m):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))
d = [q]*n
ans = [-1]*n
for i in range(len(c)):
    d[c[i]] = 0
    ans[c[i]] = c[i]
for i, j in enumerate(h):
    r[j] = i
while h:
    if len(h)>1:
        k = minimum(h)
    else:
        k = h.pop()
        if d[k] == q:
            break
        for v, w in g[k]:
            if d[v] > d[k] + w:
                d[v] = d[k] + w
                up(h, r[v])
                ans[v] = ans[k]
print(*ans, sep = '\n')
'''
'''
#D
from collections import deque
def up(n, m, h, o, distance):
    thelast={}
    path=[]
    for i in range(n):
        thelast[(i, 1)] = float('inf')
        thelast[(i, -1)] = float('inf')
    thelast[(h, 1)] = 0
    q = deque([(h, 1)])
    while q:
        curv = q.popleft()
        sg = curv[1]
        for k in distance[curv]:
            if thelast[(k[0],-1 * sg)] > thelast[curv] + k[2]:
                thelast[(k[0], -1 * sg)] = thelast[curv] + k[2]
                q.append((k[0], -1 * sg))
    q.append((o, 1))
    path.append(o)
    ih = thelast[(o, 1)]
    if ih == float('inf'):
        print(-1)
        return
    while q:
        curv = q.popleft()
        sg = curv[1]
        for k in distance[curv]:
            if k[1] != sg:
                if ih - k[2] == thelast[(k[0], -1 * sg)]:
                    ih = thelast[(k[0],-1 * sg)]
                    q.append((k[0], -1 * sg))
                    path.append(k[0])
                    break
    print(*path[::-1])
n, m = map(int, input().split())
mks = {}
for i in range(n):
        mks[(i,1)] = set()
        mks[(i,-1)] = set()
for i in range(m):
    f, l, w = map(int, input().split())
    mks[(f, -1)].add((l, 1, w))
    mks[(f, 1)].add((l, -1, w))
    mks[(l, -1)].add((f, 1, w))
    mks[(l, 1)].add((f, -1, w))
k1 = int(input())
for j in range(k1):
    h, o = map(int, input().split())
    up(n, m, h, o, mks)
'''
