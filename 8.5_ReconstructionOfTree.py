n = int(input())
pre = list(map(int, input().split()))
ino = list(map(int, input().split()))
ans = []
index = 0


def m():
    reconstruct(0, n)


def reconstruct(l_i, r_i):
    if l_i >= r_i:
        return
    global index
    c = pre[index]
    index += 1
    m_i = ino.index(c)
    reconstruct(l_i, m_i)
    reconstruct(m_i + 1, r_i)
    ans.append(c)


if __name__ == '__main__':
    m()
    print(*ans)
