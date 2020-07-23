from collections import deque
n, q = map(int, input("test").split())
t = 0
f = lambda x, y: [x, int(y)]
que = deque([f(*input().split()) for _ in range(n)])
while que:
    n, t_t = que.popleft()
    if t_t > q:
        t_t -= q
        t += q
        que.append([n,t_t])
    else:
        t += t_t
        print(f'{n} {t}')

