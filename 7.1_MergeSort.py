cnt = 0
def merge(A, l, mid, r):
    global cnt
    L = A[l:mid]
    R = A[mid:r]
    L.append(1000000001)
    R.append(1000000001)
    i = 0
    j = 0
    for k in range(l,r):
        cnt += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def mergeSort(A, l, r):
    if l + 1 < r:
        mid = int((l + r) / 2)
        mergeSort(A, l, mid)
        mergeSort(A, mid, r)
        merge(A, l, mid, r)


def m():
    global cnt
    n = int(input())
    *A, = map(int, input().split())
    l = 0
    mergeSort(A, l, n)
    print(' '.join(map(str, A)))
    print(cnt)

if __name__ == '__main__':
    m()

