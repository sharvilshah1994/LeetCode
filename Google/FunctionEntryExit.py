i1 = 't1 , "main" , entry'
i2 = 't2 , "foo" , entry'
i3 = 't3 , "bar" , entry'
i4 = 't4 , "bar" , exit'
i5 = 't5 , "foo" , exit'
i6 = 't6 , "foo" , entry'
i7 = 't7 , "foo" , exit'
i8 = 't8 , "main" , exit'

i = [i1, i2, i3, i4, i5, i6, i7, i8]


def printFunctions(i):
    map = {}
    count = 0
    temp = 0
    l = []
    for _ in i:
        print(_)
        st = str(_).split(',')
        pos, name, type = st[0], st[1], st[2]
        name = str(name).replace('"', '')
        name = str(name).replace(' ', '')
        pos, type = str(pos).replace(' ', ''), str(type).replace(' ', '')
        if type == 'entry':
            temp = count
            map[count] = [name, pos]
            count += 1
        elif type == 'exit':
            temp -= 1
            for _ in map:
                if name in map[_] and len(map[_]) < 3:
                    map[_].append(pos)
                else:
                    continue
        else:
            return -1
    for _ in map:
        ans = map[_][0] + '(' + map[_][1] + '-' + map[_][2] + ')'
        t = ''
        if map[_][0] in l:
            c = _ - 2
        else:
            c = _
        for k in range(c):
            t += '\t'
        t += ans
        l.append(map[_][0])
        print(t)


printFunctions(i)
