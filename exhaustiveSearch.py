n = int(input())
A = list(map(int, input().split()))
q = int(input())
M = list(map(int, input().split()))


def solve(i, m):
    if m == 0:
        return True
    if i > n-1 or m < 0:
        return False

    return solve(i+1, m) or solve(i+1, m-A[i])


for m in M:
    i = 0
    print("yes") if solve(i, m) else print("no")