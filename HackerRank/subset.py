case_number = int(input())


for _ in range(case_number):
    N = input()
    A = set(input().split())
    M = input()
    B = set(input().split())

    intersection = B.intersection(A)
    i = 0
    for ele in intersection:
        if ele in B:
            i += 1
    if i == len(A):
        print(True)
    else:
        print(False)
