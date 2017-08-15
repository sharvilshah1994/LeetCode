def lengthOfLongestSubstring(s):
    dic = {}
    j, ans = 0, 0
    for i in range(0, len(s)):
        if s[i] in dic:
            j = max(dic[s[i]], j)
        ans = max(ans, i - j + 1)
        dic[s[i]] = i + 1
    return ans

print(lengthOfLongestSubstring('aabbc'))
