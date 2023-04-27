f = open('rock_paper_scissors.txt','r')
one_line_list = f.read().split('\n')
point=0
for strategy in one_line_list:
    if strategy[0] == 'A':
        if strategy[2] == 'X':
            point += 3
        if strategy[2] == 'Y':
            point += 4
        if strategy[2] == 'Z':
            point += 8
    if strategy[0] == 'B':
        if strategy[2] == 'X':
            point += 1
        if strategy[2] == 'Y':
            point += 5
        if strategy[2] == 'Z':
            point += 9
    if strategy[0] == 'C':
        if strategy[2] == 'X':
            point += 2
        if strategy[2] == 'Y':
            point += 6
        if strategy[2] == 'Z':
            point += 7

print(point)