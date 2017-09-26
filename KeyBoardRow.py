def KeyboardRow(words):
    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '{', '}', '[', ']', '|']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ':', ';', '"', "'"]
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm', '<', ',', '.', '>', '?', '/']
    temp = []
    for _ in words:
        flag = ''
        for k in _:
            if k.lower() in row1:
                if flag != '1' and flag != '':
                    temp.append(_)
                    break
                else:
                    flag = '1'
            elif k.lower() in row2:
                if (flag != '2') and (flag != ''):
                    temp.append(_)
                    break
                else:
                    flag = '2'
            elif k.lower() in row3:
                if flag != '3' and flag != '':
                    flag = '3'
                    temp.append(_)
                    break
                else:
                    flag = '3'
    for _ in temp:
        words.remove(_)
    return words

print(KeyboardRow(["Hello", "Alaska", "Dad", "Peace"]))