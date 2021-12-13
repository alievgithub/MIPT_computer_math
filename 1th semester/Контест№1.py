'''
a = int(input())
c = input()
b = int(input())
if c=='>':
	if a > b:
		print("YES")
	else:
		print("NO")
else:
	if a < b:
		print("YES")
	else:
		print("NO")
'''
'''
a = int(input())
b = int(input())
c = int(input())

if a>c:
	d=c
	c=a
	a=d
if b>c:
	d=c
	c=b
	b=d
if a>b:
	d=b
	b=a
	a=d
if a+b>c:
	if a**2 + b**2 == c**2:
		print("right")
	else:
		if a**2 + b**2 > c**2:
			print("acute")
		else:
			print("obtuse")
else:
	print("impossible")
'''
'''
a = int(input())
c=0
for i in range(a):
	b = float(input())
	c += b
print(c)
'''
'''
a = int(input())
b = input()
c=0	
if b=='monkey':
	c=a/90
if b=='parrot':
	c=a/10
if b=='elephant':
	c=a/300
c=int(c)
if c==0:
	c=1
print(c)
'''
