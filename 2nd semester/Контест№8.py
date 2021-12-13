'''
#A
from collections import deque

n, m, x, y = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
dist = [None] * n
start_vertex = x
dist[start_vertex] = 0
queue = deque([start_vertex])

parents = [None] * n


while queue:
    current_vertex = queue.popleft()
    for neighbor in graph[current_vertex]:
        if dist[neighbor] is None:
            dist[neighbor] = dist[current_vertex] + 1
            parents[neighbor] = current_vertex
            queue.append(neighbor)

end_vertex = y
path = [end_vertex]
parent = parents[end_vertex]
while not parent is None:
    path.append(parent)
    parent = parents[parent]
print(len(path) - 1)
'''
'''
#B
from collections import deque

n, m = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)
dist = [None] * n
start_vertex = 0
dist[start_vertex] = 0
queue = deque ([start_vertex])

parents = [None] * n


while queue:
    current_vertex = queue.popleft()
    for neighbor in graph[current_vertex]:
        if dist[neighbor] is None:
            dist[neighbor] = dist[current_vertex] + 1
            parents[neighbor] = current_vertex
            queue.append(neighbor)
            print(current_vertex, neighbor)
'''
'''
#C
from collections import deque

def breadth_search(start):
    dist = [None]*n
    parent = [None]*n
    dist[start] = 0
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for i in graph[current]:
            if dist[i] is None:
                dist[i] = dist[current] + 1
                parent[i] = current
                queue.append(i)
            elif i == start:
                length = dist[current] - dist[i] + 1
                path = []
                tmp = current
                while tmp is not None:
                    path.append(tmp)
                    tmp = parent[tmp]
                return length, path[::-1]
    return -1, []

n, m = map(int, input().split())
graph = {i: set() for i in range(n)}
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
shortest = -1
short_path = []
for i in range(n):
    start = i
    length, path = breadth_search(start)
    if length != -1 and (shortest == -1 or length < shortest):
        shortest = length
        short_path = path
if short_path != []:
    print(*short_path)
else:
    print("NO CYCLES")
'''
'''
#D
def test(a, v0, w0, un, n, m):
    v = []
    v.append(v0 - un)
    for i in range(-un + 1, un):
        v.append(v0 + i)
        v.append(v0 + i)
    v.append(v0 + un)
    w = []
    w.append(w0)
    for j in range(1, un + 1):
        w.append(w0 - j)
        w.append(w0 + j)
    s = w[len(w) - 3::-1]
    w = w + s
    for i in range(len(v)):
        if -1 < v[i] < n and -1 < w[i] < m:
            if a1[v[i]][w[i]] == 1:
                return un
    return test(a1, v0, w0, un + 1, n, m)

n, m = map(int, input().split())
a1 = []
for i in range(n):
    a1.append(list(map(int, input().split())))
b = list([['a']*m]*n)
for i in range(n):
    for j in range(m):
        if a1[i][j] == 1:
            b[i][j] = 0
        else:
            b[i][j] = test(a1, i, j, 1, n, m)
    print(*b[i])
'''
'''
#E
from collections import deque

def add_edge(v1, v2):
    graph[v1].add(v2)
    graph[v2].add(v1)

x, y = input().split()

letters = 'abcdefgh'
numbers = '12345678'
graph = dict()

for l in letters:
    for n in numbers:
        graph[l+n] = set()


for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j]
        v2 = ''
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i + 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            v2 = letters[i - 2] + numbers[j + 1]
            add_edge(v1, v2)
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i + 1] + numbers[j + 2]
            add_edge(v1, v2)
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            v2 = letters[i - 1] + numbers[j + 2]
            add_edge(v1, v2)

dist = {v: None for v in graph}
dist[x] = 0
queue = deque([x])


while queue:
    current_vertex = queue.popleft()
    for neighbor in graph[current_vertex]:
        if current_vertex == y:
            if dist[y] % 2 == 0:
                print(dist[y] // 2)
            else:
                print(-1)
            break
        if dist[neighbor] is None:
            dist[neighbor] = dist[current_vertex] + 1
            queue.append(neighbor)
'''
