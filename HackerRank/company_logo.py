from collections import Counter


def company_logo(string):
    s = list(string)
    new_list = sorted(Counter(s).items(), reverse=True)
    new_list.sort(key=lambda x:x[1])
    print(new_list)
    for i in range(3):
        print(*new_list[-1-i])


if __name__ == '__main__':
    s = input()
    company_logo(s)