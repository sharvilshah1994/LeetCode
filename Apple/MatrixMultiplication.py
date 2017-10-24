def rotate(matrix):
    n = len(matrix)
    matrix.reverse()
    for _ in range(n):
        for k in range(_):
            matrix[_][k], matrix[k][_] = matrix[k][_], matrix[_][k]
    print(matrix)


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
