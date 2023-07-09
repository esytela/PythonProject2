'''
힙 (Heap)
    최대값 및 최소값 찾아내는 연산을 빠르게 하귀 위해 고안된
    완전 이진트리를 (complete binary tree) 기본으로 자료구조
'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, val)

    def pop(self):
        return heapq.heappop(self.heap)

#실행코드
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('>>>>>>>>>MinHeap<<<<<<<<<<') #MinHeap이니까 높은 숫자일수록 밑으로 감
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val) #기본값이 val이기에 이걸 (-)로 바꾸기만 하면 된다

    def pop(self):
        return -heapq.heappop(self.heap)


heap = MaxHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('>>>>>>>>>MaxHeap<<<<<<<<<<')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())