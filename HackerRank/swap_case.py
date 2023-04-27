def swap_case(s):
    lowercase_list = []
    new_string = []
    for i in range(ord('a'), ord('z') + 1):
        lowercase_list.append(chr(i))
    for ch in s:
        if ch in lowercase_list:
            new_string.append(ch.upper())
        else:
            new_string.append(ch.lower())
    return "".join(new_string)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
