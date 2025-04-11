

def check_for_larger(numbers: list):
    false_number =0
    for i in range(len(numbers)-1):
        if numbers[i] >= numbers[i+1]:
            false_number += 1
        elif numbers[i+1] - numbers[i] > 3:
            false_number += 1
    if false_number > 1:
        return False
    return True


def check_for_smaller(numbers: list):
    false_number = 0
    for i in range(len(numbers)-1):
        if numbers[i] <= numbers[i+1]:
            false_number += 1
        elif numbers[i] - numbers[i+1] > 3:
            false_number += 1 
    if false_number > 1:
        return False
    return True

safe_report = 0
index = 0
# with open("input.txt") as f:
#     for report in f:
#         numbers = report.split()
#         numbers = [int(i) for i in numbers]
#         if numbers[index] > numbers[index+1]:
#             if check_for_smaller(numbers):
#                 safe_report += 1
#         elif numbers[index] < numbers[index+1]:
#             if check_for_larger(numbers):
#                 safe_report += 1

# print(safe_report)

with open("input.txt") as f:
    for report in f:
        numbers = report.split()
        numbers = [int(i) for i in numbers]
        if check_for_smaller(numbers) or check_for_larger(numbers):
            safe_report += 1
print(safe_report)