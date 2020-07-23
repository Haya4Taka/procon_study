n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

c = 0
for t in T:
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if S[mid] == t:
            c += 1
            break
        elif S[mid] > t:
            right = mid - 1
        elif S[mid] < t:
            left = mid + 1


print(c)
