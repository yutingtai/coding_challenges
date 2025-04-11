import string


f = open('rocksack.txt','r')
one_line_list = f.read().split('\n')
alphabet = (string.ascii_lowercase+string.ascii_uppercase)
print(alphabet)
total = 0
for item in one_line_list:
    compartment2 = []
    size_of_item = int(len(item)/2)
    for i in range(size_of_item,len(item)):
        compartment2.append(item[i])
    print(compartment2)
    for j in range(size_of_item):
        if item[j] in compartment2:
            priority = alphabet.find(item[j])+1
            total += priority
            break
print(total)






