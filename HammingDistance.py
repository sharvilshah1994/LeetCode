def HammingDistance(x, y):
    x_bin = str('{0:0100b}'.format(x))
    y_bin = str('{0:0100b}'.format(y))
    print(x_bin)
    count = 0
    for _ in range(len(x_bin)):
        if x_bin[_] != y_bin[_]:
            count += 1
    return count

print(HammingDistance(1,4))