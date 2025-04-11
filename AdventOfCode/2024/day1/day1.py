
list1 = []
list2 = []

with open('input.txt') as f:
    for line in f:
        v1, v2 = map(int, line.split())
        list1.append(v1)
        list2.append(v2)

sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

total = 0
for i in range(len(sorted_list1)):
    if sorted_list1[i] > sorted_list2[i]:
        total += (sorted_list1[i] - sorted_list2[i])
    else:
        total += (sorted_list2[i] - sorted_list1[i])
    
print(total)



id_dict = {}

for i in sorted_list2:
    if i in id_dict:
        id_dict[i] += 1
    else:
        id_dict[i] = 1

similariry = 0
for i in sorted_list1:
    if i in id_dict:
        similariry += (i * id_dict[i])
print(similariry)