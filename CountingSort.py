def s():
    input()

    C = [0] * 10001
    B = []

    for a in map(int, input().split()):
        C[a] += 1

    i = 0
    for c in C:
        B += [str(i)]*c
        i += 1

    print(' '.join(B))


if __name__ == "__main__":
    s()
