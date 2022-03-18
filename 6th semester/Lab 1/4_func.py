from sympy import Symbol, ln, Float, solve, tan

a = -1
b = 0.5

x = Symbol('x')
f = pow(x, 5)/(1 - tan(pow(x, 7)))


"""
For every method we will have different h
"""


f_1 = f.diff(x)  # This is the first derivative of f
f_2 = f_1.diff(x)  # This is the second
f_4 = f_2.diff(x).diff(x)  # This is the 4th


h = 0.00001


def aver_rectangle(f, h, a):

    n = int((b - a) / h)
    res = 0
    for i in range(n):
        res += (h * f.subs(x, (a + h/2) + i*h))
    return res


def right_rectangle(f, h, a):

    n = int((b - a) / h)
    res = 0
    for i in range(n):
        res += (h * f.subs(x, a + i * h))
    return res


def trapezoidal(f, a, b, h):

    n = int((b - a) / h)
    result = 0.5*f.subs(x, a) + 0.5*f.subs(x, b)
    for i in range(n):
        result += f.subs(x, a + i*h)
    result *= h
    return result


def simpsons(f, a, b, h):

    tmp_sum = float(f.subs({x: a})) + \
              float(f.subs({x: b}))
    n = int((b - a) / h)
    for step in range(n):
        if step % 2 != 0:
            tmp_sum += 4 * float(f.subs({x: a + step * h}))
        else:
            tmp_sum += 2 * float(f.subs({x: a + step * h}))

    return tmp_sum * h / 3


# print(aver_rectangle(f, h, a))  # Ans = -0.111595650530556
# print(aver_rectangle(f, 2*h, a)) # Ans = -0.111595650555926

# print(right_rectangle(f, h, a))  # Ans = -0.111597763090279

# print(trapezoidal(f, a, b, h))  # Ans = -0.111597605609942

# print(simpsons(f, a, b, h)) # Ans = -0.11159825732843703
