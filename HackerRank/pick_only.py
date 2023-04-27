import collections

K = int(input())
list_of_room = input().split()
set_of_room = set(list_of_room)


set_type_of_room = set()
for number in set_of_room:
    if number not in set_type_of_room:
        set_type_of_room.add(number)

for number in set_type_of_room:
    set_of_room.remove(number)

captain_room = set_type_of_room.difference(set_of_room)

print(set_type_of_room)
print(list_of_room)
print(captain_room)

# for room in captain_room:
 #   print(room)

captain = [k for k, v in collections.Counter(list_of_room).items() if v == 1]
for i in captain:
    print(i)
