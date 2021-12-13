'''
#A
x=int(input())
h=0
n=2
while n!=x:
	if x%n==0:
		print('0')
		h=1
		break
	n+=1
if h!=1:	
	print('1')
'''
'''
#B
x=int(input())
l=x
n=1
while x>1:
	if x==1:
		print(1)
		break
	n+=1
	if n==l:
		x=int(x)
		print(x)
		break
	while x%n==0:
		print(n)
		x/=n
'''
'''
#C
x=int(input())
l=x
n=0
k=0
i=0
while k<x:
	n+=1
	k=n**3
if k>x:
    n-=1
    k=n**3
while n>0 and k!=x:
    x-=k
    i=0
    k=0
    while k<x:
    	i+=1
    	k=i**3
    if k==x:
        break
    x=l
    n-=1
    k=n**3
if k==x:
        if n>i:
                print(i, n)
        else:
                print(n, i)
else:
	print('impossible')
'''
'''
#D
def isprime(x):
    if x==1:
        return False
    for l in range(2, x):
        if x%l==0:
            return False
    return True
k=int(input())
i=2
a=0
while a!=k:
    if isprime(i)==True:
        number=i
        a+=1
    i+=1
print(number)
'''
'''
#E
k=i=1
r=last=nFumber=0
x, y=map(int, (input().split(' ')))
if x>9*y or y>x:
		print('impossible')
else:
		while y-k>-1:
			r=0
			if x-i<=9*(y-k):
				f=10**(y-k)
				number+=i*f
				last+=i
				x-=i
				r=1
				i=1
			else:
				i+=1
			if y-k==0:
				number+=x
				break
			if r==1:
				k+=1
		print(number)
'''
'''
#F
def fact(x):
    return x // 5 + fact(x // 5) if x else 0
print(fact(int(input())))
'''

