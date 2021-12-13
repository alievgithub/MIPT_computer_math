'''
#A
n = int(input())
arr = []
for _ in range(n):
    word = input().lower()
    arr.append(word)
dict = {}
ans, quan = 0, 0
for i in arr:
    j = dict.get(i, 0) + 1
    dict[i] = j
    if j > quan:
        ans, quan = i, j
print(ans, quan)
'''
'''
#B
n, m = map(int, input().split())
arr = n*[0]
for _ in range(m):
    j, k = map(int, input().split())
    arr[j] += 1
    arr[k] += 1
reg = 1
for i in range(n-1):
    if arr[i] != arr[i+1]:
        reg = 0
if reg == 1:
    print('YES')
else:
    print('NO')
'''
'''
#C
from collections import deque
n, m = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
distances = [None] * n
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])
parents = [None] * n
while queue:
    cur_v = queue.popleft()
    for neigh_v in graph[cur_v]:
        if distances[neigh_v] is None:
            distances[neigh_v] = distances[cur_v] + 1
            parents[neigh_v] = cur_v
            queue.append(neigh_v)
for i in range(len(distances)):
    print(distances[i])
'''
