def lcs(x, y):
    c = []
    m = len(x)
    n = len(y)
    maxl = 0
    for i in range(m+1):
        l = []
        for j in range(n+1):
            if i == 0 or j == 0:
                l.append(0)
            else:
                l.append(None)
        c.append(l)

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = c[i][j-1]
            maxl = max(maxl, c[i][j])

    return maxl


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        X = input()
        Y = input()
        print(lcs(X, Y))
