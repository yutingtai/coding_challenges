from itertools import groupby

group = []
for k , g in groupby(input()):
    group.append(list(g))

compress = []
for number in group:
    compress.append((len(number),int(number[0])))

print(*compress)