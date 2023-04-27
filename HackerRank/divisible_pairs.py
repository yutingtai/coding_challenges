def divisibleSumPairs(n, k, ar):
    pairs = 0
    for i in range(n-1):
        for j in range(len(ar[i:-1])):
            if (ar[i] + ar[i+j+1]) % k == 0:
                pairs += 1
    print(pairs)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)
