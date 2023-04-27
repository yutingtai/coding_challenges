A = input()
set_a = set(input().split())
N = int(input())
update_list = []
compared_list = []
for _ in range(N):
    update_list.append(input().split())
    compared_list.append(input().split())

sub_set_list = []
for sub in compared_list:
    sub_set = set(sub)
    sub_set_list.append(sub_set)

for i, step in enumerate(update_list):
    if step[0] == 'intersection_update':
        set_a.intersection_update(sub_set_list[i])
    elif step[0] == 'update':
        set_a.update(sub_set_list[i])
    elif step[0]  == 'symmetric_difference_update':
        set_a.symmetric_difference_update(sub_set_list[i])
    elif step[0] == 'difference_update':
        set_a.difference_update(sub_set_list[i])

sum = 0
for ele in set_a:
    sum += int(ele)

print(sum)
# print(update_list)
# print(sub_set_list)