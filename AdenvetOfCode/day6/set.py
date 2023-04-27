f = open('input.txt', 'r')
f_list = list(f)
# print(len(*f_list))
# first part
for i in range(0,len(*f_list)):
     first_set = set([char for char in f_list[0][0 + i:4 + i]])
     if len(first_set) == 4:
         print(i+4)
         break

# second part
# for i in range(0, len(*f_list)):
#     second_set = set([char for char in f_list[0][0 + i:14 + i]])
#     if len(second_set) == 14:
#         print(i + 14)
