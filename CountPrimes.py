def countPrimes(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for j in range(2, n + 1):
        if j > 2:
            flag = False
            for i in range(2, j):
                if j % i == 0:
                    flag = True
            if not flag:
                count += 1
    return count

print(countPrimes(4))