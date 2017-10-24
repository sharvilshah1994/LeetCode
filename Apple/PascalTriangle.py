def pascalTriangle(numRows):
    if numRows <= 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        row = [0] + triangle[-1] + [0]
        triangle.append([row[j] + row[j + 1] for j in range(i + 1)])
    return triangle

print(pascalTriangle(5))