M = input()
a = input()
a_list = list(map(int, a.split()))
N = input()
b = input()
b_list = list(map(int, b.split()))

a_set = set()
b_set = set()
for num_a in a_list:
    a_set.add(num_a)

for num_b in b_list:
    b_set.add(num_b)

lis = []
for i in a_set.difference(b_set):
    lis.append(i)
for i in b_set.difference(a_set):
    lis.append(i)
lis.sort()
print(*lis, sep = '\n')
