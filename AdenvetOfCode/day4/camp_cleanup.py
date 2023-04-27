f = open('pairs_of_ID.txt', 'r')
one_line_list = f.read().split('\n')
number_of_fully_contained = 0
number_of_overlap = 0
pairs = []
for line in one_line_list:
    pairs.append(line.split(','))

begin = 0
end = 1


def contains(interval, number):
    return interval[begin] <= number <= interval[end]


for pair in pairs:
    first_interval = [int(x) for x in pair[0].split('-')]
    second_interval = [int(x) for x in pair[1].split('-')]
    if contains(second_interval, first_interval[begin]) and contains(second_interval, first_interval[end]):
        number_of_fully_contained += 1
    elif contains(first_interval, second_interval[begin]) and contains(first_interval, second_interval[end]):
        number_of_fully_contained += 1

print(number_of_fully_contained)

for pair in pairs:
    first_interval = [int(x) for x in pair[0].split('-')]
    second_interval = [int(x) for x in pair[1].split('-')]
    if contains(second_interval, first_interval[begin]) or contains(second_interval, first_interval[end]):
        number_of_overlap += 1
    elif contains(first_interval, second_interval[begin]) or contains(first_interval, second_interval[end]):
        number_of_overlap += 1

print(number_of_overlap)