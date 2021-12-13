'''
#A
def matryoshka(n):
	if n == 1:
		print('matryoshechka')
	else:	
		print('verh matryoshki ' + str(n))
		matryoshka(n-1)
		print('niz matryoshki ' + str(n))

#n = int(input())
#maximum = n
#print(matryoshka(n))
'''
'''
#B
def F(n):
	if n == 0:
		return 1
	return n - M(F(n-1))
def M(n):
	if n == 0:
		return 0
	return n - F(M(n-1))

#n = int(input())
#print(F(n))
#print(M(n))
'''
'''
#C
def f(K, M):
	if M == 1:
		return K
	return K + f(K+1, M-1) + K

#K = int(input())
#M = int(input())
#print(f(K, M))
'''
'''
#D
def make_exchange(money, coins):
	coins.sort()
	def f(money, coinstype):
		if money == 0:
			return 1
		if money < 0 or coinstype == 0:
			return 0
		else:
			return f(money, coinstype - 1) + f(money - change(coinstype), coinstype)
	def change(coinstype):
		global coins
		return coins[coinstype - 1]
	return f(money, len(coins))

#money, coins = input().split()
#money = int(money.strip(","))
#coins = list(map(int, coins.strip("[]").split(",")))
#print(make_exchange(money, coins))
'''
'''
#E
def is_add_35(n):
	if n < 1:
		return False
	if n == 1:
		return True
	return (is_add_35(n-3) or is_add_35(n-5))

#N = int(input())
#print(is_add_35(N))
'''
'''
#F
arr = list(map(int, input().split()))
def k1(arr):
    if len(arr) > 1:
        print(*arr)
        return (k1(arr[1:]))
    else:
        return arr
def k2(arr):
    if len(arr)>1:
        print (*k2(arr[:(len(arr) - 1)]))
    return (k1(arr))
print(*k2(arr))
'''
