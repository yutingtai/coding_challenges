from collections import OrderedDict

ordered_dict = OrderedDict()

for _ in range(int(input())):

    my_list = input().split()

    price = int(my_list[-1])

    key = ' '.join(map(str, my_list[:-1]))

    if key in ordered_dict:
        ordered_dict[f'{key}'] += price
    else:
        ordered_dict[f'{key}'] = price


for key, value in ordered_dict.items():
    print(key, value)