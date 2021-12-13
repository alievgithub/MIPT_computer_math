'''
# «Неограниченный» полиномиальный хеш
B = 37

def poly_hash(s):
  h = 0
  for c in s:
    h = h * B + ord(c) - ord('a') + 1
    return h

print(poly_hash('qwfdvf'))
'''
'''
# Полиномиальный хеш по модулю
B = 37
# Subtraction has more priority than `shift left`
M = (1 << 61) - 1

def poly_hash(s):
    h = 0
    for c in s:
        h = (h * B + ord(c) - ord('a') + 1) % M
    return h
'''
'''
# Алгоритм Рабина-Карпа
def poly_hash(s):
    h = [0] # Array of hashes for all prefixes
    for c in s:
        h.append((h[-1] * B + ord(c) - ord('a') + 1) % M)
    return h
'''
'''
# Хеш-таблица (demo)
TABLE_SIZE = 10 ** 5 + 7
def get_pos(key):
    h = poly_hash(key)
    return (h % TABLE_SIZE, h)
'''
'''
# Хеш-таблица (full)
def add(table, key):
    pos, h = get_pos(key)
    for e in table[pos]:
        if e[0] == h:
            print(key, "is already in table")
            return
    table[pos].append([h, key])
def find(table, key):
    """
    Returns:
        True, if key is in table.
        False, otherwise.
    """
    pos, h = get_pos(key)
    for e in table[pos]:
        if e[0] == h:
            return True
    return False

def delete(table, key):
    pos, h = get_pos(key)
    for i, e in enumerate(table[pos]):
        if e[0] == h:
            table[pos].pop(i)
            return
    print(key, "is not in table")

#Создание пустой таблицы в начале программы:
table = [[] for _ in range(TABLE_SIZE)]
'''
