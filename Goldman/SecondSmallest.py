def secondSmallest(l):
    if len(l) < 2:
        return 0
    else:
        l.sort()
        return l[1]


print(secondSmallest([1, 4, 2, 3, 4, 5]))
