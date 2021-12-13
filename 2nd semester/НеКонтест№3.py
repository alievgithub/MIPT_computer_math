'''
#A
def students(learners_french, pianists, swimmers):
    learners_french = set(learners_french)
    pianists = set(pianists)
    swimmers = set(swimmers)
    a = swimmers & pianists
    return a.difference(learners_french)

learners_french = ['Иван', 'Николай']
pianists = ['Иван', 'Артем', 'Кирилл']
swimmers = ['Иван', 'Артем', 'Кирилл', 'Антон']
print(students(learners_french, pianists, swimmers))
'''
'''
#B
def unique_num(list1, list2):
    list1 = set(list1)
    ans1 = len(list1)
    list2 = set(list2)
    ans2 = len(list2)
    list3 = list1.union(list2)
    ans3 = len(list3)
    return ans1, ans2, ans3

list1 = [1, 1, 2, 3]
list2 = [1, 1, 2, 2, 3, 4]
print(unique_num(list1, list2))
'''
'''
#C
A = set()
while True:
    num = int(input())
    if num in A:
        print('Встречалось')
    else:
        print('Не встречалось')
    A.add(num)
'''

''' Предыдущие три задачи отметили на парах '''

'''
#D

# В конце вводимого списка написать 'stop'

voting = dict()
film = str(input())
while film != 'stop':
    if film in voting.keys():
        voting[film] += 1
    else:
        voting[film] = 1
    film = str(input())
f_list = list(voting.items())
f_list.sort(key = lambda i: i[1])
n = len(f_list)
for i in range(n):
    print(f_list[n-i-1][0], f_list[n-i-1][1])
'''