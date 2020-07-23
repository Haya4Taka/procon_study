n = int(input())
array = list(map(int, input().split()))

for i in range(n):
    print(' '.join(map(str, array)))
    I = i + 1
    if I > n - 1:
        break

    J = I - 1
    v = array[I]
    while J >= 0 and array[J] > v:
        array[J+1] = array[J]
        J -= 1
    array[J+1] = v

