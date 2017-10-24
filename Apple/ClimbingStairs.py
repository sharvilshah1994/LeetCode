def ClimbingStairs(n):
    if n == 1:
        return 1
    res = [0 for k in range(n)]
    res[0], res[1] = 1, 2
    for k in range(2, n):
        res[k] = res[k-1] + res[k-2]
    return res[-1]

print(ClimbingStairs(10))