'''
a=int(input())
b=int(input())
i=a
while i>1:
	if a%i==0 and b%i==0:
		break
	else: 
		i-=1 
print(i)
'''
'''
n=1
i=0
while n!=0:
	n=int(input())
	if n%2==0 and n!=0:
		i+=1
print(i)
'''
'''
n=1
k=j=i=0
while n!=0:
	n=int(input())
	if n==0:
		break
	k+=n
	j+=n**2
	i+=1
M=k/i
D=j/i - M**2
M=round(M, 3)
D=round(D, 3)
print(M, D)
'''
'''
n=int(input())
k=1000001
r=1000000
j=0
i=1
l=0
h=0
word=input()
for x in word.split():
	x=int(x)
	l+=1
	if k>x:	
		r=k
		k=x
		v=l
	if r>x and x>=k and l!=v:
		r=x
	if j<x:
		i=j
		j=x
		h=l
	if i<x and x<=j and l!=h:
		i=x
print (k+r, j+i)			
'''
'''
x=1
sup=k=-1001
i=n=0
while x!=0: 
	x=int(input())
	if x==0:
		break
	n+=1
	if x>=sup:
		sup=x
		if k!=sup:
			i=0
		k=sup
		i+=1

print(n-i)
'''
'''
#Важно!!!
line=input()
i=0
number=len(line)
mas=[]
while i<number:
	line_int=''
	a=line[i]
	while '0'<=a<='9':
		line_int+=a
		i+=1
		if i<number:
			a=line[i]
		else:
			break
	i+=1
	if line_int!='':
		mas.append(int(line_int))
x=max(mas)
print(x)
'''
'''
speed=number=0
mas=[]
k=0
i=1
while number!='A999AA':
	speed, number=input().split()
	speed=int(speed)daw ardour.
	if number=='A999AA':
		break
	number_int=''
	a=number[i]
	b=number[i+1]
	c=number[i+2]
	if (a==b and b==c and a==c) and speed>60:
		k+=1000
	elif (a==b or b==c or a==c) and (speed>60):
		k+=500
	elif speed>60:
		k+=100
	
print(k)
'''
'''
x=-1
k=max=0
while x!=0:
	last=x
	x=int(input())
	if x==0:
		break
	if x>last and x>max:
		k+=1
	if x>max:
		max=x
print(k)
'''
'''
x=int(input())
i=npnumber=0
while x!=0:
	k=x%10
	npnumber+=k*((-10)**i)	
	i+=1
	x=x/10
	x=int(x)
print(npnumber)inconsistent use of tabs and spaces in indentation
'''
'''
#Разобраться!!!
x=int(input())
oldnumber=l=''
number=0
i=1
while x!=0:
	number=x%(60**i)
	x-=number
	number/=(60**(i-1))
	i+=1
	while number%10!=0:
		l='v'
		oldnumber=l+oldnumber
		number-=1
	while number!=0:
		l='<'
		oldnumber=l+oldnumber
		number-=10
	if x>0:
		oldnumber='.'+oldnumber
print(oldnumber)
'''
