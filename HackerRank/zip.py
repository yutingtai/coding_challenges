N, X = map(int, input().split())
scores = []
for _ in range(X):
    scores.append(input().split())


student_scores = list(zip(*scores))
list_scores = []
for student in student_scores:
    list_scores.append(list(map(float,student)))

for scores in list_scores:
    total = 0
    for i in range(len(scores)):
        total += scores[i]
    ave = total/X
    print(ave)






