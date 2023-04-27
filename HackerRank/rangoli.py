# size = 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# size = 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# left_mirror arr: ['f', 'e', 'd', 'c', 'b']
# ['b', 'c', 'd', 'e', 'f', 'e', 'd', 'c', 'b']

def generate_letters(starting_letter, count):
    starting_letter_num = ord(starting_letter)
    arr = [chr(i) for i in range(starting_letter_num, starting_letter_num + count)]
    return arr


def left_mirror(arr):
    tail = arr[1:]
    reverse_tail = tail[::-1]
    return reverse_tail + arr


def generate_center(starting_char, count):
    letters = generate_letters(starting_char, count)
    mirror_letters = left_mirror(letters)
    return '-'.join(mirror_letters)


# center: "dog", size: 5 ---> "-dog-"
# center: "cat", size: 9 --> "---cat---"
def pad(center, size):
    half = (size - len(center)) // 2
    return ('-' * half) + center + ('-' * half)


def print_rangoli(size):
    width = (size - 1) * 2 + size * 2 - 1
    middle_column = generate_center('a', size)
    middle_column_arr = middle_column.split('-')

    center_widths = []
    for i in range(size, 0, -1):
        center_widths.append(i)
    center_widths = left_mirror(center_widths)

    for index, element in enumerate(middle_column_arr):
        center = generate_center(element, center_widths[index])
        row = pad(center, width)
        print(row)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)





