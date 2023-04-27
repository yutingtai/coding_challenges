# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations


input_user = input().split()
string = input_user[0]
length = int(input_user[1])
string_list = []
for ch in string:
    string_list.append(ch)
string_list.sort()

list_user = []
for size in range(1,length+1):
    list_user.append(list(combinations(''.join(string_list), size )))

for item in list_user:
    for substring in item:
        tuple_to_list = list(substring)
        print(''.join(tuple_to_list))