import random

def game(a, b):
    n = 0
    while a*b != 0:
        coin = random.uniform(0, 1)
        if coin < 0.5:
            a += 1
            b -= 1
        else:
            a -= 1
            b += 1
        n += 1
    return n

A = 8
B = 20
draw = 0
N = 100
for i in range(N):
    draw += game(A, B)

print(draw/N)
