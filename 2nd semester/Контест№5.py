'''
#A
cards = list(map(str, input().split()))
buy = 0
for i in range(1, len(cards)):
    card1 = list(cards[i-1])
    card2 = list(cards[i])
    a = int(card2[1])
    b = int(card1[1])
    if card2[0] == card1[0] and abs(a - b) <= 2:
        buy += 2
        if cards[0][0] == cards[i-2][0]:
            buy += 2
print(buy)
'''
'''
#B
mas = list(map(str, input().split()))
stack =[]
result = k = 0
for i in range(len(mas)):
    x = mas[i]
    if x != '#' and x != '%':
        stack.append(float(x))
    elif x =='#':
        l = len(stack)
        for j in range(l):
            result += stack.pop()
        stack.append(result)
    elif x == '%':
        if len(stack) >=2:
            a = stack.pop()
            b = stack.pop()
            result = b*(a/100)
            stack.append(result)
        else:
            k = 1
            break
if k != 1:
    print(stack.pop())
else:
    print(float(0))
'''
'''
#C
import operator

def calc(expr):
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    stack = [0]
    for token in expr.split(" "):
        if token in operators:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(operators[token](op1, op2))
        elif token:
            stack.append(float(token))
    return stack.pop()

temp = None
ar = []
while temp != "=":
    temp = input()
    if temp == "=":
        break
    ar.append(temp)
instr = ' '.join(ar)
print(int(calc(instr)))
'''
'''
#D
import heapq

n = int(input())
a = list(map(int, input().split()))
heapq.heapify(a)
print(*a)
'''
'''
#E
def max_heapify(arr, heap_size,i):
   l=2*i+1
   r=2*i+2
   if l <heap_size and A[l]>A[i]:
      largest = l
   else:
      largest = i
   if r<heap_size and arr[r]>arr[largest]:
      largest = r
   if largest!=i:
      arr[largest], arr[i] = arr[i], arr[largest]
      max_heapify(arr, heap_size,largest)
def build_max_heap(arr):
   for i in range(len(arr)//2, -1, -1):
      max_heapify(arr, len(arr), i)
def heapsort(arr):
   build_max_heap(arr)
   heap_size=len(arr)
   print(*arr)
   for i in range(len(arr)-1, 0, -1):
       arr[0], arr[i] = arr[i], arr[0]
       heap_size -=1
       max_heapify(arr, heap_size, 0)
       print(*arr)
'''
