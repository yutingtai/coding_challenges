f = open('input_calories.txt', 'r')
one_line_list = f.read().split('\n')
total_cal = 0
max = 0
second = 0
third = 0
number_of_elf = 0
for calorie in one_line_list:
    if calorie != '':
        total_cal += int(calorie)
    else:
        number_of_elf += 1
        if total_cal > max:
            second = max
            max = total_cal
        if max > total_cal > second:
            third = second
            second = total_cal
        total_cal = 0
print(max,number_of_elf)
print(max+second+third)


