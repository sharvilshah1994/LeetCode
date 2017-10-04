# def rearrangeWord(word):
#     last = word[len(word) - 1]
#     index = 0
#     flag = False
#     for _ in range(len(word) - 2, -1, -1):
#         if word[_] < word[_+1]:
#             index = _
#             flag = True
#             break
#
#     if not flag:
#         return "no answer"
#
#     second_index = 0
#     for _ in range(len(word)-1, -1, -1):
#         if word[_] > word[index]:
#             second_index = _
#             flag = True
#             break
#
#     if flag:
#         word = swap(word, index, second_index)
#         word = ''.join(word[:index+1]) + ''.join(sorted(word[index+1:]))
#         return word
#     return "no answer"
#
#
# def swap(s, i, j):
#     return ''.join((s[:i], s[j], s[i + 1:j], s[i], s[j + 1:]))
#
#
# print(rearrangeWord('beec'))


