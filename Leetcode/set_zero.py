def set_zero(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    index_zero = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                index_zero.append([row, col])
    for index in index_zero:
        for i in range(len(matrix)):
            matrix[i][index[1]] = 0
        for j in range(len(matrix[0])):
            matrix[index[0]][j] = 0


def main():
    mat = [[0, 1, 2, 0],
           [3, 4, 5, 2],
           [1, 3, 1, 5]]

    mat2 = [[0,1]]

    set_zero(mat)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j])


if __name__ == '__main__':
    main()
