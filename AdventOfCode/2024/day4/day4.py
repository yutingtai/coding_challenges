import time
from typing import Iterator


def get_slice_window(grid, target: str) -> Iterator:
    rows = len(grid)
    cols = len(grid[0].split()[0])
    target_len = len(target)

    for i in range(rows - (target_len - 1)):
        for j in range(cols - (target_len - 1)):
            window = [grid[i + k][j : j + target_len] for k in range(target_len)]
            yield window


def count_horizontal(line, target):
    count = 0
    for i in range(len(line) - len(target) + 1):
        string = line[i : i + len(target)]
        if string == target:
            count += 1
        elif string[::-1] == target:
            count += 1
    return count


def count_vertical(line, target):
    count = 0
    for i in range(len(line) - len(target) + 1):
        string = line[i : i + len(target)]
        if string == target or string[::-1] == target:
            count += 1
    return count


def count_diagonal(window, target):
    count = 0
    ltor = [window[i][i] for i in range(len(target))]
    rtol = [window[i][len(target) - 1 - i] for i in range(len(target))]
    ltor_str = "".join(ltor)
    rtol_str = "".join(rtol)

    # Compare both diagonals and their reverses with the target
    for s in [ltor_str, rtol_str]:
        if s == target or s[::-1] == target:
            count += 1
    return count


def count_XMAS(grid):
    target = "XMAS"

    windows = get_slice_window(grid, target)

    ver = 0
    dia = 0
    hor = 0
    for window in windows:
        dia += count_diagonal(window, target)

    cols = len(grid[0].split()[0])
    for i in range(cols):
        column = "".join(row[i] for row in grid)
        ver += count_vertical(column, target)

    for line in grid:
        hor += count_horizontal(line.strip(), target)

    print(hor + ver + dia)


def check_diagonal(window, target):
    ltor = [window[i][i] for i in range(len(target))]
    rtol = [window[i][len(target) - 1 - i] for i in range(len(target))]
    ltor_str = "".join(ltor)
    rtol_str = "".join(rtol)

    # Compare both diagonals and their reverses with the target
    if (ltor_str == target or ltor_str[::-1] == target) and (
        rtol_str == target or rtol_str[::-1] == target
    ):
        return True
    return False


def count_X_MAS(grid):
    target = "MAS"
    windows = get_slice_window(grid, target)
    total = 0
    for window in windows:
        if check_diagonal(window, target):
            total += 1

    print(total)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.readlines()
        count_XMAS(data)
        count_X_MAS(data)
