#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    starting_page = (p - 1) // 2 + 1
    if p-n == 0:
        min_page = 0
    elif p % 2 == 0:
        page = (n - p) // 2
        if page < starting_page:
            min_page = page
        else:
            min_page = starting_page
    else:
        page = (n - p) // 2 + 1
        if page < starting_page:
            min_page = page
        else:
            min_page = starting_page
    print(min_page)


if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)
