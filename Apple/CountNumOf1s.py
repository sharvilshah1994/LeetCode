def countOnes(num):
    num = '{0:10b}'.format(num)
    count = 0
    for _ in str(num):
        if _ == '1':
            count += 1
    return count

print(countOnes(2))