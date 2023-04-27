from collections import defaultdict

n, m = input().split()
arr_A = []
arr_B = []
for i in range(int(n)):
    arr_A.append(input())
for i in range(int(m)):
    arr_B.append(input())

d = defaultdict(list)


for i, el_A in enumerate(arr_A):
    d[f'{arr_A[i]}'].append(f'{i + 1}')

for el_B in arr_B:
    if el_B in d:
        print(*d[el_B])
    else:
        print(-1)


