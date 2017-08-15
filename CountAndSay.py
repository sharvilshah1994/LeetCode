def countAndSay(n):
    s = ['1']
    result = '1'
    # The n-th sequance, input 1 should output '1'
    for i in range(n - 1):
        start = 0
        temp = []
        # Process one sequence, scan from start to end
        while start < len(s):
            count = 1
            next = start + 1
            # Scan until s[next] is different
            while next < len(s) and s[start] == s[next]:
                next += 1
                count += 1
            # Get the new items in
            temp.append(str(count))
            temp.append(s[start])
            # Start from next one
            start = next
        # Concatenate list into string, using "," as separator in default
        result = ''.join(temp)
        s = temp
    return result

print(countAndSay(10))