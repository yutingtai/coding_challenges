def print_formatted(number):
    # your code goes
    longest_number = '{0:b}'.format(n)
    l = len(longest_number)
    for i in range(1, n + 1):
        num = str(i)
        octal = '{0:o}'.format(i)
        hexa = '{0:x}'.format(i).upper()
        bina = '{0:b}'.format(i)
        print( num.rjust(l), '{0:o}'.format(i).rjust(l), '{0:x}'.format(i).upper().rjust(l), '{0:b}'.format(i).rjust(l))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
