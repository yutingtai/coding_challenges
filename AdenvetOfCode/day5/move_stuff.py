import pandas as pd


df = pd.read_fwf('stuff.txt',
                 header=None,
                 names=range(1,10))
stacks = []
for i in range(1,10):
    stacks.append([stuff for stuff in df[i] if not (pd.isnull(stuff)) == True and not stuff.isdigit() ])

for i in stacks:
    i.reverse()

f = open('step.txt', 'r')
one_line_list = f.read().split('\n')
steps = []
for i in one_line_list:
    steps.append([int(s) for s in i.split() if s.isdigit()])

for step in steps:
    num_of_boxes, from_stack_id, to_stack_id = step
    from_stack_index = from_stack_id - 1
    to_stack_index = to_stack_id - 1
    for i in range(int(num_of_boxes)):
        stacks[to_stack_index].append(stacks[from_stack_index][-(i+1)])
    for i in range(int(num_of_boxes)):
        stacks[from_stack_index].pop(-1)


for step in steps:
    num_of_boxes, from_stack_id, to_stack_id = step
    from_stack_index = from_stack_id - 1
    to_stack_index = to_stack_id - 1
    for i in range(int(num_of_boxes)):
        stacks[to_stack_index].append(stacks[from_stack_index][-num_of_boxes+i])
    for i in range(int(num_of_boxes)):
        stacks[from_stack_index].pop(-1)


for i in stacks:
    print(i[-1],end="")
print(stacks)