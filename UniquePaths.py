def uniquePaths(m, n):
    if m == 1 or n == 1:
        return 1
    m -= 1
    n -= 1
    if m < n:
        m = m + n
        n = m - n
        m = m - n
    res = 1
    j = 1
    for i in range(m + 1, m + n + 1):
        res *= i
        res /= j
        j += 1
    return int(res)

print(uniquePaths(10,10))