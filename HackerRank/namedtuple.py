from collections import namedtuple

N = int(input())
title = ','.join(input().split())
Student = namedtuple('Student',title)
sum = 0
for _ in range(N):
    student_info = input().split()
    student = Student(student_info[0],student_info[1],student_info[2],student_info[3])
    sum += int(student.MARKS)
ave = sum/N
print("{:.2f}".format(ave))

