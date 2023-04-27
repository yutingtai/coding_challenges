import string


f = open('rocksack.txt','r')
one_line_list = f.read().split('\n')
alphabet = (string.ascii_lowercase+string.ascii_uppercase)
print(alphabet)
total = 0

for j in range(0,int(len(one_line_list)),3):
    for item in one_line_list[j]:
        compartment2 = [x for x in one_line_list[j + 1]]
        compartment3 = [x for x in one_line_list[j + 2]]
        if (item in compartment2) and compartment3:
            priority = alphabet.find(item) + 1
            print(item, priority)
            total += priority
            break
print(total)





