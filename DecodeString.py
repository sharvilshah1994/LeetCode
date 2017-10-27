def decodeString(s):
    ans = ''
    stack = []
    t = ''
    for _ in s:
        if _ == '[':
            pass
        elif _ == ']':
            while not is_digit(stack[-1]):
                t += stack.pop()
            i = int(stack.pop())
            for k in range(i):
                ans += t
            t = ''
            stack.append(ans)
            ans = ''
        else:
            stack.append(_)
    return ans[::-1]

def is_digit(s):
    try:
        i = int(s)
        return True
    except:
        return False


print(decodeString("2[b3[a]]"))