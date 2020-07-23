n = int(input())
*a, = map(int, input().split())
c = 0
flag = True
while flag:
    flag = False
    for i in range(n - 1, 0, -1):
        if a[i] < a[i-1]:
            v = a[i]
            a[i] = a[i-1]
            a[i-1] = v
            flag = True
            c += 1

print(*a)
print(c)