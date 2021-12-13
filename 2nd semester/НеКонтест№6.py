'''
#Работа с файлами
import operator
import numpy as np
file = open ("C:/Users/theto/OneDrive/Рабочий стол/task1.txt")
for line in file:
    line = line.strip()
    new_list = line.split(' ')
    a = np.array(new_list)
    a = np.array(a).astype(np.float)
    print(np.mean(a))
'''
'''
#Подсчет асимптотиик
import numpy as np
import matplotlib.pyplot as plt
import time
random_list_of_nums = [9, 1, 15, 28, 6]
results = []
def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert

for i in range(1, 201):
   random_list_of_nums = np.random.rand(i)

   start = time.time()  # начало замера
   insertion_sort(random_list_of_nums)
   print(random_list_of_nums)
   end = time.time()  # конец замера
   s1 = end-start
   results.append(s1)
print(results)

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(1, 200, 200)  # отрезок [0, 4π] из 200 точек
yline = results

# добавление графиков
plt.plot(x, results, label = 'скорость работы алгоритма', color = 'red', linewidth = 2)

# название всего графика и подписи к осям
plt.title('Асимптотика сортировки вставками')
plt.xlabel('абсцисса')
plt.ylabel('ордината')

# ограничение видимой области графика
plt.xlim(1, 200)
plt.ylim(0.0001, 0.0055)

# отметки на абсциссе, первый аргумент - положения, второй - подписи
plt.xticks([0, 20, 40 , 60 , 80, 100 , 120 , 140, 160, 180 , 200])

plt.grid()  # сетка по отметкам на осях
plt.legend()  # подписи графиков

plt.show()
# plt.savefig('temp.png', dpi=90)  # расскомментировать для сохранения картинки
'''
'''
#Снежинки
import turtle
import math

# Get the screen size and set some scaling
wn = turtle.Screen()
wx = wn.window_width()*.5
wh = wn.window_height()*.5
base_triangle_length = 2.0/math.sqrt(3.0)*wh

# Parameters of the Koch triangle
depth = 2

# Set up the turtle
Koch = turtle.Turtle()
Koch.speed(50*(depth+1))
Koch.penup()
Koch.setposition((-wx/2, -wh/2))
Koch.pendown()
Koch.left(60)

def draw_koch_segment(t, run, mydepth, depth):
  if mydepth == depth:
    # Just draw a segment
    t.fd(run)
  else:
    myrun = run/3.0
    # Make each straight bit into a smaller version of ourselves
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.left(60)
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.right(120)
    draw_koch_segment(t, myrun, mydepth+1, depth)
    t.left(60)
    draw_koch_segment(t, myrun, mydepth+1, depth)

# Draw the basic triangle outline
for i in range(3):
  draw_koch_segment(Koch, base_triangle_length, 0, depth)
  Koch.right(120)
'''
'''
#Калькулятор
import re
def tokenze(code:str)->list:
    return code.split()
def op_prior(char_op:str):
    if char_op == "^":
        return 6
    elif char_op == "*":
        return 5
    elif char_op == "/":
        return 5
    elif char_op == "%":
        return 3
    elif char_op == "+":
        return 2
    elif char_op == "-":
        return 2
def isOp(c:str)->bool:
    if c == "-" or c == "+" or c == "*" or c == "/" or c == "^": return True
    return False
def opn(code:str)->None:
    p = 0
    op_stack: list = []
    res: list = []
    while True:
        v = code[p]
        p += 1
        if v == ';':
            break
        if re.match("[0-9]+[.]*[0-9]*", v) or re.match("[A-Za-z]+", v):
            res.append(v)
        elif isOp(v):
                while(len(op_stack) > 0 and
                op_stack[-1] != "(" and
                op_prior(v) <= op_prior(op_stack[-1])):
                    res.append(op_stack.pop())
                  #if len(op_stack)==0: raise RuntimeError("No left paren")
                op_stack.append(v)
        elif v == ')':
            while len(op_stack) > 0:
                x = op_stack.pop()
                if x == '(' :
                    break
                res.append(x)
        elif v == "(":
            op_stack.append(v)
    while len(op_stack)>0 :
           res.append(op_stack.pop())
              #if op_stack[-1]=="(":
                  #raise RuntimeError("No right paren")
    return res
'''
'''
#Найдии рыбу
a = ''

with open("C:/Users/theto/OneDrive/Рабочий стол/find_a_fish.txt") as file:
    for line in file:
        #a += (repr(line))
        a += line.strip()

print(a)
print(len(a))

index = 0
a = a[:index] + a[index+1:]
print(a)

index = 0
a = a[:index] + a[index+1:]
print(a)

res1_new = []
res1 = a.split(">2")
for val in res1:
    # срезаю пробелы
    val = val.strip()
    # формирую новый массив
    res1_new.append(val)
print(res1_new)

test1 = res1_new[0]
print(test1)


res2_new = []
res2 = res1_new[1].split(">3")
for val in res2:
    # срезаю пробелы
    val = val.strip()
    # формирую новый массив
    res2_new.append(val)
print(res2_new)

test2 = res2_new[0]
print(test2)

res3_new = []
res3 = res2_new[1].split(">4")
for val in res3:
    # срезаю пробелы
    val = val.strip()
    # формирую новый массив
    res3_new.append(val)
print(res3_new)

test3 = res3_new[0]
print(test3)

test4 = res3_new[1]
print(test4)
print('Аминокислотные последовательности:', test1, test2, test3, test4, sep = '\n')

#test1, test2 , test3, test4 - строки, содеражщие аминокислотные последовательности

def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

print(distance(test3,test1))
print(distance(test3,test2))
print(distance(test3,test4))

print('Аминоксилотная последовательность рыбы находится под номером 3, так как для нее сумма редакционных расстояний максимальна')
'''
