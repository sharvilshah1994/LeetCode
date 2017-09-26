encrypted_message = 'tcez fqg'
j = 0
k = list(encrypted_message)
key = 8251220
for i in range(len(encrypted_message)):
    if j > len(str(key)) - 1:
        j = 0
    s = int(ord(k[i]) - int(str(key)[j]))
    if 65 <= ord(k[i]) <= 90:
        if s <= 65:
            diff = 65 - s
            add = 91 - diff
            k[i] = chr(add)
        else:
            k[i] = chr(s)
        j += 1
    elif 97 <= ord(k[i]) <= 122:
        if s <= 97:
            diff = 97 - s
            add = 123 - diff
            k[i] = chr(add)
        else:
            k[i] = chr(s)
        j += 1

print (''.join(k))