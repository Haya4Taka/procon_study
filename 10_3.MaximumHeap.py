import math
h = 0
heap = [None]

def max_heapify(index):
    left_i = index * 2
    right_i = (index * 2) + 1

    if left_i <= h and heap[left_i] > heap[index]:
        largest = left_i
    else:
        largest = index
    if right_i <= h and heap[right_i] > heap[largest]:
        largest = right_i

    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        max_heapify(largest)

def build_maxheap(start_i):
    for index in range(start_i, 0, -1):
        print(index)
        max_heapify(index)

def main():
    global h
    h = int(input())
    heap.extend(map(int, input().split()))
    start_i = math.floor(h/2)
    build_maxheap(start_i)
    heap.pop(0)
    print(heap)


if __name__ == '__main__':
    main()