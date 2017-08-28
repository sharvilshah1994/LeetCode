def swapLexOrder(str, pairs):
    map, res = {}, list(str)
    roots = [-1] * len(str)

    def find(roots, i):
        if roots[i] == -1:
            return i
        roots[i] = find(roots, roots[i])
        return roots[i]

    for pair in pairs:
        tmp1 = find(roots, pair[0] - 1)
        tmp2 = find(roots, pair[1] - 1)
        if tmp1 != tmp2:
            roots[tmp1] = tmp2
    for i in range(len(roots)):
        tmp = find(roots, i)
        if map.get(tmp, 'x') == 'x':
            map[tmp] = [i]
        else:
            map[tmp].append(i)

    for k, v in map.items():
        tmp = sorted([str[x] for x in v])[::-1]
        for i, x in enumerate(sorted(v)):
            res[x] = tmp[i]
    return ''.join(res)

print(swapLexOrder("abdc", [[1, 4], [3, 4]]))