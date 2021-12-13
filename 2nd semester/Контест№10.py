'''
#C
n, m = map(int, input().split())
a = []
b = [i for i in range(n)]
t = m
for f in range(m):
    cnt = 0
    u, v = map(int, input().split())
    if b[u] != b[v]:
        j = b[v]
        for i in range(n):
            if b[i] == j:
                b[i] = b[u]
    for i in range(1, n):
        if b[i] != b[i - 1]:
            cnt += 1
            break
    if cnt == 0:
        t = f + 1
        break
print(t)
'''
'''
#A
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
input()
l = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        if a[i][j] == 1 and l[i] != l[j]:
            cnt += 1
print(cnt)
'''
'''
#B
from collections import deque

def bfs(start):
    dist = [None]*n
    parent = [None]*n
    dist[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for i in graph[u]:
            if dist[i] is None:
                dist[i] = dist[u] + 1
                parent[i] = u
                queue.append(i)
            elif i == start:
                l = dist[u] - dist[i] + 1
                path = []
                tmp = u
                while tmp is not None:
                    path.append(tmp)
                    tmp = parent[tmp]
                return l, path[::-1]
    return -1, []

n, m = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1 - 1].add(v2 - 1)
shortest = -1
shortpath = []
for i in range(n):
    start = i
    l, path = bfs(start)
    if l != -1 and (shortest == -1 or l < shortest):
        shortest = l
        shortpath = path
if shortpath != []:
    print("No")
else:
    print("Yes")
'''
'''
#D
n, m = map(int, input().split())
a = {i: set() for i in range(n)}
for i in range(m):
    u, v, w = map(int, input().split())
    a[u].add((v, w))
    a[v].add((u, w))
d = [(-1, -1, float("inf"))]*n

for v, w in a[0]:
    d[v] = (0, v, w)

t = {i for i in range(1, n)}
edges = []
weight = 0
for _ in range(n - 1):
    j = -1
    minw = float("inf")
    for v in t:
        if d[v][2] < minw:
            minw = d[v][2]
            j = v
    edges.append((d[j][0], d[j][1]))
    weight += minw
    t.remove(j)
    for v, w in a[j]:
        if w < d[v][2]:
            d[v] = (j, v, w)
print(weight)
for i in range(len(edges)):
    print(" ".join(map(str, edges[i])))
'''
