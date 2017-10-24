class Solution(object):
    def reverse_words_in_sentence(self, sentence):
        ans = ''
        word = str(sentence).split(' ')
        for i in range(len(word) - 1, -1, -1):
            if ans:
                ans += ' ' + word[i]
            else:
                ans += word[i]
        ans = ' '.join(ans.split())
        ans = ans.strip()
        return ans


inp = 'the     sky    is       blue'
print(Solution().reverse_words_in_sentence(inp))