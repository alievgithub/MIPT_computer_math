import matplotlib.pyplot as mp
import math
def fx(n, r, x0):
    y = [x0]
    def f(x):
            y = x * (math.exp(r * (1 - x)))
            return y
    for i in range(int(n) - 1):
        y.append(f(y[-1]))
    g = y[-1]
    return g
def re(n, r, x0):
    a=[]
    k=[]
    while r <= 6:
        k.append(fx(n, r, x0))
        a.append(r)
        r += 0.01
    return k, a
n = 700
for i in range(300):
    x, y = re(n, 1, 5)
    n += 1
    mp.plot(y, x, 'ko', markersize = 0.02)
mp.show()

r1 = 2
r2 = 2.53
r3 = 2.66
r4 = 2.69
delta1 = (r2 - r1)/(r3 - r2)
delta2 = (r3 - r2)/(r4 - r3)
print("Delta 1", delta1)
print("Delta 2", delta2)
