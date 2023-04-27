def count_substring(string, sub_string):
    string = string
    sub_string = sub_string
    len_s = len(sub_string)
    i = 0
    j = 0
    while i <= len(string):
        if string[0+i:len_s+i] == sub_string:
            j += 1
        i += 1
    return j


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)