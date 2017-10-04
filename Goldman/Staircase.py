# A program to count the number of ways to reach n'th stair

# Recursive function used by countWays
def countWaysUtil(n, m):
    res = [0 for x in range(n)]  # Creates list res witth all elements 0
    res[0], res[1] = 1, 1

    for i in range(2, n):
        j = 1
        while j <= m and j <= i:
            res[i] = res[i] + res[i - j]
            j = j + 1
    return res[n - 1]


# Returns number of ways to reach s'th stair
def countWays(s, m):
    if s == 0:
        return 0
    return countWaysUtil(s + 1, m)


print(countWays(5, 2))
