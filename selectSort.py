n = int(input())
*a, = map(int, input().split())
c = 0
for i in range(n):
    minj = i
    for j in range(i, n):
        if j + 1 < n and a[minj] > a[j + 1]:
            minj = j + 1

    if a[i] > a[minj]:
        v = a[i]
        a[i] = a[minj]
        a[minj] = v
        c += 1

print(*a)
print(c)

