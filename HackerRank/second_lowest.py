import math

arr = [2, 2, 4, 4, 3, 3, 5, 7, 8, 9, 3]
lowest = math.inf
second_lowest = math.inf
for el in arr:
    if el < lowest:
        second_lowest = lowest
        lowest = el
    elif lowest < el < second_lowest:
        second_lowest = el

print(lowest)
print(second_lowest)

second_lowest_indices = []

for i, el in enumerate(arr):
    if el == second_lowest:
        second_lowest_indices.append(i)

print(second_lowest_indices)