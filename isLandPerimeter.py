def islandPerimeter(grid):
    island = 0
    n = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                island += 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1: n += 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1: n += 1
    return island * 4 - n * 2

print(islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
))