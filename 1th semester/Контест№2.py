'''
a = int(input())
if ((a%4==0) and (a%100!=0)):
	print("YES")
else:
	if (a%400==0): 
		print("YES")
	else:
		print("NO")
'''
'''
a = int(input())
c=0
for i in range(3):
	b=a%10
	c+=b
	a=int(a/10)
print(c)
'''
'''
a=1
b=0
while (a!=0):
	a = int(input())
	b+=a
print(b)
'''
'''
a=1
b=-1
while (a!=0):
	a = int(input())
	b+=1
print(b)
'''
'''
a=1
b=0
c=-1
while (a!=0):
	a = int(input())
	b+=a
	c+=1
d=b/c
d=round(d,2)	
print(d)
'''
'''
a = int(input())
b=0
i=0
while (b<a):
	b=2**i
	i+=1
if (b==a):
	print("YES")
else:
	print("NO")
'''
'''
j = int(input())
i=0
a=0
b=0
c=0
d=0
while (i<j):
	x, y = input().split()
	x=int(x)
	y=int(y)
	if ((x>0) and (y>0)):
		a+=1
	elif ((x<0) and (y>0)):
		b+=1
	elif ((x<0) and (y<0)):
		c+=1
	elif ((x>0) and (y<0)):
		d+=1
	i+=1;
if ((a>=b) and (a>=c) and (a>=d)):
		print(1, a)
elif ((b>=a) and (b>=c) and (b>=d)):
		print(2, b)
elif ((c>=b) and (c>=a) and (c>=d)):
		print(3, c)
elif ((d>=b) and (d>=c) and (d>=a)):
		print(4, d)
'''
'''
b=-10001
a=1
while (a!=0):
	a=int(input())
	if (a==0):
		break
	if (a>b):
		b=a
print(b)
'''
'''
a=1
i=0
b=0
c=0
d=0
e=0
f=0
k=0
j=0
s=0
p=0
m=0
o=0
r=0
while (a!=0):
	a=int(input())
	if (a==0):
		break
	k+=1
	if (a>i):
		b=c
		c=d
		d=e
		e=f
		f=i
		i=a
		s=p
		p=m
		m=o
		o=r
		r=j
		j=k
if ((k-j) > 4):
	print(i)
elif ((k-r) > 4):
	print(f)
elif ((k-o) > 4):
	print(e)
elif ((k-m) > 4):
	print(d)
elif ((k-p) > 4):
	print(c)
elif ((k-s) > 4):
	print(b)
'''
'''
#Не работает
a=1
b=0
i=0
k=0
c=10001
while (a!=0):
	a=int(input())
	if (a==0):
		break
	b+=a
	if (a>i):
		i=a
	if (a<c):
		c=a
j=i-c+1
k=((c+i)/2)*j
k=int(k)
print(k-b)
'''
'''
a=1
b=0
j=0
k=0
while a!=0:
	a=int(input())
	if j<a:
		j=a
	if b==0:
		b=a
	if b>a and a!=0:
		b=a
	k+=a
for i in range(b, j+1):
	k-=i
print(abs(k))
'''
