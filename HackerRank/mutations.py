def mutate_string(string, position, character):
    string = s
    string_l = list(string)
    position = int(i)
    character = c
    string_l[position] = c
    new_string = ''.join(string_l)
    return new_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)