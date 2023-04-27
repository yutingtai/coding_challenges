def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    for row in range(len(matrix)):
        if matrix[row][len(matrix[0])-1] == target:
            return True
        elif len(matrix) == 1:
            for column in range(len(matrix[0])):
                if matrix[0][column] == target:
                    return True
        elif matrix[row][len(matrix[0])-1] > target:
            for column in range(len(matrix[0])):
                if matrix[row][column] == target:
                    return True

    return False


def main():
    matrix = [[1, 3, 5, 7],
              [10, 11, 16, 20],
              [23, 30, 34, 60]]

    matrix_2 = [[1],[3]]

    print(searchMatrix(matrix_2, target=3))


if __name__ == '__main__':
    main()
