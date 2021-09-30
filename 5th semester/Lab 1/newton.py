import math
from math import atan
from sympy import *

e = 0.0001; i = 1

x = Symbol('x')
#f = atan(x-1) + 2*x
f = 20*x**3 - 4*x**2 - 5*x + 1

df = f.diff(x)

#x0 = 0.5
x0 = 0.4
x1 = x0 - f/df
X0 = []
F = []
dF = []

print('  x0', '     f(x0)')

while abs(x1.subs(x, x0) - x0) > e:
    X0.append(x0)
    F.append(f.subs(x, x0))
    dF.append(df.subs(x, x0))
    x0 = x1.subs(x, x0)
    x1 = x0 - f / df
    print(i, '%.5f' % round(x0, 5), '%.5f' % round(f.subs(x, x0), 5))
    i += 1

print('   x0 =', '%.5f' % round(x0, 5))
print('f(x0) =', '%.6f' % round(f.subs(x, x0), 6))
