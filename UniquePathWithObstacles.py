def uniquePathsWithObstacles(obstacleGrid):
    if len(obstacleGrid) == 0:
        return 0
    rows = len(obstacleGrid)
    cols = len(obstacleGrid[0])
    for i in range(0, rows):
        for j in range(0, cols):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            elif i == 0 and j == 0:
                obstacleGrid[i][j] = 1
            elif i == 0:
                obstacleGrid[i][j] = obstacleGrid[i][j - 1] * 1
            elif j == 0:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] * 1
            else:
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
    return obstacleGrid[rows - 1][cols - 1]

print(uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
))