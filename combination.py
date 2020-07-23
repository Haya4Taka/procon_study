# make combination which choose any item from n items
n = int(input())


def rec(i):
    if i > n - 1:
        print(ary)
        return

    ary[i] = 0
    rec(i + 1)

    ary[i] = 1
    rec(i + 1)


# 0 represents not selected
ary = [0] * n
rec(0)


