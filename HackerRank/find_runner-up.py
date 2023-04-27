if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

new_arr = []
for current_number in list(arr):
    if current_number not in new_arr:
        new_arr.append(current_number)

new_arr.sort()
print(new_arr[-2])

