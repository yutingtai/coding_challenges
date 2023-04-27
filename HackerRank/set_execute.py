n = int(input())
s = set(map(int, input().split()))

N = int(input())
action_list_str = []
for _ in range(N):
    action_list_str.append(input())

action_list = []
for action_str in action_list_str:
    if len(action_str) > 4:
        action_list.append(action_str.split())
    else:
        no_space_action_str = str(action_str).replace(' ', '')
        action_list.append([no_space_action_str])


for action in action_list:
    if action[0] == 'pop':
        s.pop()

    elif action[0] == 'discard':
        s.discard(int(action[1]))

    elif action[0] == 'remove':
        s.remove(int(action[1]))

sum=0
for ele in s:
    sum += ele
print(sum)
