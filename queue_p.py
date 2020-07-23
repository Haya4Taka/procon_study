n, q = map(int, input().split())
t = 0
que = [input().split() for _ in range(n)]
while que:
    tsk = que.pop(0)
    tsk[1] = int(tsk[1])
    tsk_t = tsk[1]
    tsk[1] -= q
    if tsk[1] > 0:
        t += q
        que.append(tsk)
    else:
        t += tsk_t
        print(f'{tsk[0]} {t}')

