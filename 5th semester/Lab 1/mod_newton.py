import math
from math import atan
from sympy import *

a = 0; b = 1; e = 0.0001; i = 1

x = Symbol('x')
f = atan(x-1) + 2*x

df = f.diff(x)

x0 = 0.5
x1 = x0 - f/df
X0 = []
F = []
dF = []

print('  x0', '     f(x0)')

x_tmp = x0
flag = True
while abs(x1.subs(x, x0) - x0) > e:
    if abs(x1.subs(x, x0) - x0) < e + 0.006:
        flag = False
    X0.append(x0)
    F.append(f.subs(x, x0))
    dF.append(df.subs(x, x0))
    print(i, '%.5f' % round(x0, 5), '%.5f' % round(f.subs(x, x0), 5))
    x0 = x1.subs(x, x0)
    i += 1
    if flag:
        x1 = x0 - f / df
    else:
        x1 = x0 - f / df.subs(x, x_tmp)

print('   x0 =', '%.5f' % round(x0, 5))
print('f(x0) =', '%.6f' % round(f.subs(x, x0), 6))
