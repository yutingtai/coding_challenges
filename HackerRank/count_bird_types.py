from collections import Counter


def migratoryBirds(arr):
    c = Counter(arr).most_common()
    c_sort = sorted(c, key=lambda x: (-x[1], x[0]))
    print(c_sort[0][0])





if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)

