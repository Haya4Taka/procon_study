import math
heap = []


def itemprint(i, key):
    print(f'node {i+1}:', end=' ')
    print(f'key = {key},', end=' ')
    pi = math.floor(i/2)
    if pi != 0:
        print(f'parent key = {heap[pi]},', end=' ')
    li = i*2
    if len(heap) > li:
        print(f'left key = {heap[li]},', end=' ')
    ri = i*2 + 1
    if len(heap) > ri:
        print(f'right key = {heap[ri]},', end=' ')


def main():
    h = int(input())
    heap.extend(map(int, input().split()))
    for i, key in enumerate(heap):
        itemprint(i, key)


if __name__ == '__main__':
    main()