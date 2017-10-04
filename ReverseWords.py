def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    st = s.split(' ')
    ans = ''
    for _ in range(len(st) - 1, -1, -1):
        if ans:
            ans += ' ' + st[_]
        else:
            ans += st[_]
    ans = ' '.join(ans.split())
    ans = ans.lower().strip()
    return ans

print(reverseWords(' 1'))