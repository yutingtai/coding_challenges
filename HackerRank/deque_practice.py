from collections import deque


my_list = []
for _ in range(int(input())):
    my_list.append(input().split())

d = deque()
for step in my_list:
    if len(step) > 1:
        eval(f'd.{step[0]}({step[1]})')
    else:
        for remove in step:
            eval(f'd.{remove}()')

print(*d)
