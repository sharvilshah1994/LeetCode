def LUS(a, b):
    if a == b:
        return -1
    return max(len(a), len(b))

print(LUS('aba', 'cbc'))