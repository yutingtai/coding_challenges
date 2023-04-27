if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

score_list = student_marks[query_name]
sum_score = 0
for score in score_list:
    sum_score += score

ave = sum / len(score_list)

# print two decimal places
format_ave = "{:.2f}".format(ave)
print(format_ave)
