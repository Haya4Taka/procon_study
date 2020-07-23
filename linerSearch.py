n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = map(int, input().split())

count = 0
S.append(0)
for t in T:
    S[-1] = t
    i = 0
    while S[i] != t:
        i += 1
    if i != n:
        count +=1

    # for s in S:
    #     if t == s:
    #         count += 1
    #         break

print(count)
