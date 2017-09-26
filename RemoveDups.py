def removeDups(s):
    dic = {}
    for _ in range(len(s)):
        dic[s[_]] = _
    result = []
    for _ in range(len(s)):
        if result:
            if s[_] not in result:
                while s[_] < result[-1] and _ < dic[result[-1]]:
                    result.pop()
                    if not result:
                        break
                result.append(s[_])
        else:
            result.append(s[_])
    return result

print(removeDups('cbacdcbc'))
