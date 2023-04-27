if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

lowest = 100
second_lowest = 100
for student in students:
    if student[1] < lowest:
        second_lowest = lowest
        lowest = student[1]
    elif lowest < student[1] < second_lowest:
        second_lowest = student[1]


new_list = []
name_list = []
for i, el in enumerate(students):
    if el[1] == second_lowest:
        new_list.append(students[i])
for name in new_list:
    name_list.append(name[0])

name_list.sort()
for name in name_list:
    print(name)
