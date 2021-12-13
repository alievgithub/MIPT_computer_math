'''
#A
def test_brackets(brackets):
    while '()' in brackets or '[]' in brackets or '{}' in brackets:
        brackets = brackets.replace('()', '')
        brackets = brackets.replace('[]', '')
        brackets = brackets.replace('{}', '')
    return not brackets

brackets = input()
print("YES") if test_brackets(brackets) == True else print("NO")
'''
'''
#B
n = int(input())
arr = list(map(int, input().split()))
k = 0
arr = [0] + arr
for i in range(n, 1, -1):
    if arr[i//2] < arr[i]:
        k = 1
        break
print("NO") if k == 1 else print("YES")
'''
'''
#D
n = int(input())
que = []
for i in range(n):
    com = input().split()
    if com[0] == '+':
        que.append(com[1])
    elif com[0] == '*':
        que.insert((len(que)+1) // 2, com[1])
    elif com[0] == '-':
        print(que.pop(0))
'''
'''
#C
def list_to_array(linked_list, head):
    result = []
    for i in linked_list:
        if i[0] == head[0]:
            n = head[1]
            result.append(head[0])
    for i in range(len(linked_list) - 1):
        result.append(linked_list[n][0])
        n = linked_list[n][1]
    return result

'''
'''
#F
n, honesty = map(int, input().split())
heroes = []
for i in range(n):
    s = input().split()
    heroes.append(s)
k = int(input())
i = 0
for _ in range(k):
    if len(heroes) == 1:
        break
    else:
        if heroes[i % len(heroes)][1] == '0' and honesty == 0:
            heroes[i % len(heroes)][1] = '1'
            honesty = 1
            i += 1
        elif heroes[i % len(heroes)][1] == '0' and honesty == 1:
            honesty = 0
            i += 1
        elif heroes[i % len(heroes)][1] == '1' and honesty == 0:
            del heroes[i % len(heroes)]
        elif heroes[i % len(heroes)][1] == '1' and honesty == 1:
            i += 1
for i in range(len(heroes)):
    print(*heroes[i])
'''
