n, k = map(int, input().split())
parcels = []


def fold(lst, p):
    track = 1
    cur_sum = 0
    for i in lst:
        if cur_sum + i <= p:
            cur_sum += i
        else:
            track += 1
            cur_sum = i

    return track


for _ in range(n):
    parcels.append(int(input()))

left = max(parcels)
right = 100000 * 10000

while right - left > 0:
    mid = (left + right) // 2
    track = fold(parcels, mid)

    if track <= k:
        right = mid
    else:
        left = mid + 1

print(left)
