def main():

    l = [1,1]


    n = int(input())

    if n < 2:
        print(1)
        exit()

    for i in range(2, n+1):
        t = l[i-1] + l[i-2]
        l.append(t)

    print(l[-1])


if __name__ == "__main__":
    main()

