import math
from math import atan

#a = 0; b = 1; e = 0.0001; i = 1
a = 0.4; b = 1; e = 0.0001; i = 1
#def f(x):
#    return atan(x-1) + 2*x
def f(x):
    return 20*x**3 - 4*x**2 - 5*x + 1
y1 = f(a); y2 = f(b)
if (y1 * y2 > 0) or (y1 * y2 == 0):
    print("no solutions")
else:
    n = 1
    x = (a+b)/2
    y3 = f(x)
    print('  ', ' a', '      b', '      (a+b)/2', 'f((a+b)/2)', 'f(a)', '    f(b)')
    while (abs(y3) > e):
        if i > 9:
            print(i, end = '. ')
        else:
            print(i, end = '.  ')
        print('%.5f' % round(a, 5),  '%.5f' % round(b, 5), end = ' ')
        x = (a+b)/2
        print('%.5f' % round(x, 5), end = ' ')
        if f(x) < 0:
            print('%.5f' % round(f(x), 5), end = '   ')
        else:
            print('%.5f' % round(f(x), 5), end = '    ')
        print('%.5f' % round(f(a), 5), '%.5f' % round(f(b), 5))
        i += 1
        y3 = f(x);
        if y1 * y3 < 0:
            b = x
        else:
            a = x
            n += 1
    print('   x = %.5f' % round(x, 5))
    print('f(x) = %.5f' % round(f(x), 5))
