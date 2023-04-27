from collections import Counter


def sockMerchant(n, ar):
    c = Counter(ar)
    pair = 0
    values = c.values()
    for value in values:
        pair += value % 2

    print(pair)
    print(c)


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
