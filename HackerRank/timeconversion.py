#!/bin/python3
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hh = s[0:2]
    mm = s[3:5]
    ss = s[6:8]
    if 'PM' in s:
        if hh != '12':
            print(f'{int(hh) + 12}:{mm}:{ss}')
        else:
            print(f'12:{mm}:{ss}')
    if 'AM' in s:
        if hh != '12':
            print(f'{hh}:{mm}:{ss}')
        else:
            print(f'00:{mm}:{ss}')


if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
