from itertools import permutations

input_user = input().split()
string = input_user[0]
length = int(input_user[1])
list_user = list(permutations(f'{string}', length))
list_user.sort()
for item in list_user:
    tuple_to_list = list(item)
    print(''.join(tuple_to_list))


