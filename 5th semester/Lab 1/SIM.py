import math
from math import atan

e = 0.0001; i = 1
def f(x):
    return atan(x-1) + 2*x

def phi(x):
    return -atan(x-1)/2

x0 = 0.5
x1 = phi(x0)
X1 = []
X0 = []
print('  x0', '     f(x0)')
while abs(x0 - x1) > e:
    X1.append(x1)
    X0.append(x0)
    x0 = x1
    x1 = phi(x1)
    print(i, '%.5f' % round(x0, 5), '%.5f' % round(f(x0), 5))
    i += 1

print('   x0 =', '%.5f' % round(x0, 5))
print('f(x0) =', '%.5f' % round(f(x0), 5))
