# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
if __name__ == '__main__':
    operation_list = []
    N = int(input())
    for _ in range(N):
        operation = input()
        operation_list.append(operation.split())

arr = []
for do in operation_list:
    if do[0] == 'insert':
        arr.insert(int(do[1]), int(do[2]))
    elif do[0] == 'print':
        print(arr)
    elif do[0] == 'remove':
        arr.remove(int(do[1]))
    elif do[0] == 'append':
        arr.append(int(do[1]))
    elif do[0] == 'sort':
        arr.sort()
    elif do[0] == 'pop':
        arr.pop()
    elif do[0] == 'reverse':
        arr.reverse()

