def ReverseNum(num):
    if num < 0:
        return -ReverseNum(-num)
    return int(str(num)[::-1])

print(ReverseNum(-123))

#
# if x < 0:
#             return -self.reverse(-x)
#         result = 0
#         while x:
#             result = result * 10 + x % 10
#             x /= 10
#         return result if result <= 0x7fffffff else 0