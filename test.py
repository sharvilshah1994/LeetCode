def simplifyPath(path):
    st = path.split('/')
    stack = []
    for i in st:
        if st == '.':
            continue
        if st == '..':
            if len(stack):
                stack.pop()
            continue
        if len(i) < 1:
            continue
        stack.append(i)
    p = ''
    for x in stack:
        p += '/'+str(x)
    if p == '':
        return '/'
    else:
        return p

print(simplifyPath("/home/a/./x/../b//c/"))