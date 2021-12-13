'''
#A
n = int(input())
m = [[int(j) for j in input().split()] for i in range(n)]
x = True
y = True
z = True

for i in range(n):
    for j in range(n):
        if (i == j) and m[i][j] == 1:
            x = False
            break
    for i in range(n):
        for j in range(n):
            if (m[i][j] != m[j][i]):
                y = False
                break
            else:
                z = True

if x and y and z:
    print("YES")
else:
    print("NO")
'''
'''
#B
n = int(input())
m = [input().split() for i in range(n)]
for i in range(n):
    for j in range(n):
        if m[i][j] != "0":
            print(i, j, m[i][j])
'''
'''
#C
quan1 = int(input())
quan2 = int(input())
arr = []
for i in range(quan2):
    arr.append(list(map(int, input().split())))

def digraph(quan1, arr):
    for i in range(quan1):
        for j in range(quan1):
            list = []
            if test(i, j, quan1, arr, list) == False:
                return 'NO'
    return 'YES'

def test(n, m, quan1, arr, list):
    list.append(n)
    if n == m:
        return True
    else:
        end = []
        for i in range(len(arr)):
            if arr[i][0] == n and (arr[i][1] in list) == False:
                end.append(arr[i][1])
        for e in end:
            if test(e, m, quan1, arr, list) == True:
                return True
    return False

print(digraph(quan1, arr))
'''
'''
#D
def dfs(vertex, g):
    used[vertex] = 1
    for neighbor in g[vertex]:
        if used[neighbor] == 0:
            dfs(neighbor, g)
        elif used[neighbor] == 1:
            stack.append(neighbor)
            exit(0)
    used[vertex] = 2

def dfs_cycle(vertex, g):
    cycle.append(vertex)
    used[vertex] = 1
    for neighbor in g[vertex]:
        if used[neighbor] == 0:
            dfs_cycle(neighbor, g)
        elif used[neighbor] == 1:
            print(*cycle)
            break
    used[vertex] = 2

if __name__ == "main":
    n, m = map(int, input().split())
    g = [[] for i in range(n)]

    for j in range(m):
        start, finish = map(int, input().split())
        g[start].append(finish)
    used = [0] * n
    cycle = []
    stack = []
    for i in range(n):
        if used[i] == 0:
            dfs(i, g)

    if len(stack) == 0:
        print("YES")
    else:
        used = [0] * n
        dfs_cycle(stack[0], g)
'''
'''
#E
def dfs(vertex, g):
    used[vertex] = 1
    for neighbor in g[vertex]:
        if used[neighbor] == 0:
            dfs(neighbor, g)
        elif used[neighbor] == 1:
            stack.append(neighbor)
            print("NO")
            exit(0)
    used[vertex] = 2

def dfs_cycle(vertex, g, visited):
    visited[vertex] = True
    for neighbor in g[vertex]:
        if not visited[neighbor]:
            dfs_cycle(neighbor, g, visited)
    ans.append(vertex)

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[] for i in range(n)]

    for j in range(m):
        start, finish = map(int, input().split())
        g[start].append(finish)
    used = [0] * n
    cycle = []
    stack = []
    for i in range(n):
        if used[i] == 0:
            dfs(i, g)

    if len(stack) == 0:
        visited = [False] * n
        ans = []
        for i in range(n):
            if not visited[i]:
                dfs_cycle(i, g, visited)
        ans[:] = ans[::-1]
        print(*ans)
'''
