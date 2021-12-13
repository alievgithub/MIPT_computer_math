'''
#A
import math
x1, y1, r1 = input().split()
x2, y2, r2 = input().split()
x1 = int(x1)
y1 = int(y1)
r1 = int(r1)
x2 = int(x2)
y2 = int(y2)
r2 = int(r2)
dist = (x1-x2)**2 + (y1-y2)**2
if abs(r2-r1) <= math.sqrt(dist) <= r2+r1:
    print('YES')
else:
    print('NO')
'''
'''
#B
a, b = input().split()
c, d = input().split()
n = int(input())
a = int(a)
b = int(b)
c = int(c)
d = int(d)
p = k = 0
while n != 0:
    e, f = input().split()
    e = int(e)
    f = int(f)
    p += 1
    n -= 1
    if 4*((e-a)**2 + (f-b)**2) <= (e-c)**2 + (f-d)**2:
        break
if p == 0 or p == n:
    print('-1')
else:
    print(p)
'''
'''
#C
a, b, c, d, e, f = input().split()
g, h = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
x1 = g - a
y1 = h - b
x2 = g - c
y2 = h - d
x3 = g - e
y3 = h - f
print(x1+g, y1+h, x2+g, y2+h, x3+g, y3+h)
'''
'''
#D
a, b, c, d = input().split()
e, f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
if c == a:
    xb, yb = 2* c - e, f
    xb = round(xb, 5)
    yb = round(yb, 5)
    print(xb, yb)
else:
        a0 = (d-b)/(c-a)
        b0 = b - a0*a
        if d == b:
            print(e, 2*d - f)
        else:
            a1 = -1/a0
            b1 = f - a1*e
            x0 = (b0-b1)/(a1-a0)
            y0 = a0*x0 + b0
            x1 = 2*x0 - e
            y1 = 2*y0 - f
            x1 = round(x1, 5)
            y1 = round(y1, 5)
            print(x1, y1)
'''
'''
#E
a, b, c = input().split()
d, e, f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
if a*e == b*d:
    print('NO')
else:
    y = (d*c - f*a)/(a*e - d*b)
    x = -(b*y + c)/a
    y = round(y)
    x = round(x)
    print (x, y)
'''
'''
#F
n = int(input())
a = [[j for j in input().split()]for i in range(n)]
a1 = []
a2 = []
a3 = []
a4 = []
k1 = []
k2 = []
k3 = []
k4 = []
c = 0
d = 0
g = 0
f = 0
def line(b, x):
    for i in range(len(b)):
        k = int(b[i][1])/int(b[i][0])
        x.append(k)

for e in range(n):
    if int(a[e][0])>0 and int(a[e][1])>0:
        a1.append(a[e])
    elif int(a[e][0])<0 and int(a[e][1])>0:
        a2.append(a[e])
    elif int(a[e][0])<0 and int(a[e][1])<0:
        a3.append(a[e])
    elif int(a[e][0])>0 and int(a[e][1])<0:
        a4.append(a[e])

for j in range(n):
    if a[j][0] == 0:
        if a[j][1]>0:
            c += 1
        else:
            d += 1
    elif a[j][1]==0:
        if a[j][0]>0:
            f += 1
        else:
            g += 1

k1.append(line(a1,k1))
k1.pop(-1)
k2.append(line(a2,k2))
k2.pop(-1)
k3.append(line(a3,k3))
k3.pop(-1)
k4.append(line(a4,k4))
k4.pop(-1)
from collections import Counter
k1 = Counter(k1)
k2 = Counter(k2)
k3 = Counter(k3)
k4 = Counter(k4)

def maximum(s):
    h = []
    for m in s.items():
        h.append(m[1])
    if len(h)>0:
        v = max(h)
        return v
    else:
        return -1

s1 = maximum(k1)
s2 = maximum(k2)
s3 = maximum(k3)
s4 = maximum(k4)
z = max(c,d,f,g,s1,s2,s3,s4)
print(z)
'''
'''
#G
def inside(x0, y0, x, y):
    for j in range(n):
        if x[j]==x0 and y[j]==y0:
            return "YES"
            break
    a=0
    for i in range(n):
        if (((y[i]<=y0 and y0<y[i-1]) or (y[i-1]<=y0 and y0<y[i])) and
        (x0 > (x[i-1] - x[i]) * (y0 - y[i]) / (y[i-1] - y[i]) + x[i])):
            a = 1 - a
    if a==1:
        return 'YES'
    else:
        return 'NO'
n = int(input())
x1 = []
y1 = []
for i in range(n):
    x,y=input().split()
    x=float(x)
    y=float(y)
    x1.append(x)
    y1.append(y)
x0, y0=input().split()
x0=float(x0)
y0=float(y0)
print(inside(x0, y0, x1, y1))
'''
'''
#H
def add(a, pos, value1, value2):
    for i in range(len(a), pos, -1):
        a[i] = a[i-1]
    a[pos] = value1, value2
def area(a):
    pos = len(a)
    value1, value2 = a[0][0], a[0][1]
    k=0
    for i in range(pos):
        if i != pos-1:
            l1=((a[i][0]-a[i+1][0])**2+(a[i][1]-a[i+1][1])**2)**(1/2)
            l2=((a[i][0]-value1)**2+(a[i][1]-value2)**2)**(1/2)
            l3=((a[i+1][0]-value1)**2+(a[i+1][1]-value2)**2)**(1/2)
            p=(l1+l2+l3)/2
            q=(p*(p-l1)*(p-l2)*(p-l3))**(1/2)
        else:
            l1=((a[i][0]-a[0][0])**2 + (a[i][1]-a[0][1])**2)**(1/2)
            l2=((a[i][0]-value1)**2+(a[i][1]-value2)**2)**(1/2)
            l3=((a[0][0]-value1)**2+(a[0][1]-value2)**2)**(1/2)
            p=(l1+l2+l3)/2
            q=(p*(p-l1)*(p-l2)*(p-l3))**(1/2)
        k+=q
    return k
a = dict()
b = input().split()
while b[0]!="end":
    if b[0]=="add":
        pos, value1, value2= int(b[1]), float(b[2]), float(b[3])
        add(a,pos, value1, value2)
    elif b[0]=="area":
        print(round(area(a), 5))
    b=input().split()
'''
