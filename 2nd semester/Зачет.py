'''
#Не работает
def sift_up(heap, i):
	while i>0 and heap[(i-1)//2] > heap[i]:
		heap[(i-1)//2], heap[i] = heap[i], heap[(i-1)//2]
		i = (i-1)//2

def sift_down(heap, i):
	n = len(heap)
	while i*2 + 1 < n:
		j = i
		if heap[i] > heap[i*2 + 1]:
			j = i*2 + 1
		if i*2 + 2 < n and heap[j] > heap[i*2 + 2]:
			j = i*2 + 2
		if i == j:
			break
		heap[i], heap[j] = heap[j], heap[i]
		i = j

i = j = 0	
n, k = input().split()
n = int(n)
k = int(k)
heap = list(map(int, input().split()))
arr = []
for i in range(len(heap)):
	arr.append(heap[i])
	sift_up(arr, i)
for i in range(len(heap)):
	sift_down(arr, i)
print(*arr)
'''
'''
def sort(heap):
	for i in range(n-1):
		for j in range(n-i-1):
			if heap[j] < heap[j+1]:
				heap[j], heap[j+1] = heap[j+1], heap[j]
	
n, k = input().split()
n = int(n)
k = int(k)
heap = list(map(int, input().split()))
sort(heap)
print(*heap[0:k])
'''
