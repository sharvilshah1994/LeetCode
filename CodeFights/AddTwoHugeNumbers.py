# Definition for singly-linked list:

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None




def addTwoHugeNumbers(a, b):
    num1 = ''
    num2 = ''
    count = 0
    q = []
    while a:
        count += 1
        if count == 1:
            num1 += str(a.value)
        else:
            le = len(str(a.value))
            loop = 4 - le
            for i in range(loop):
                num1 += '0'
            num1 += str(a.value)
        a = a.next
    q.append(count)
    count = 0
    while b:
        count += 1
        if count == 1:
            num2 += str(b.value)
        else:
            le = len(str(b.value))
            loop = 4 - le
            for i in range(loop):
                num2 += '0'
            num2 += str(b.value)
        b = b.next
    q.append(count)
    m = max(q)
    ans = int(num1) + int(num2)
    ans = str(ans)[::-1]
    count = 0
    l = []
    t = ''
    for _ in range(len(str(ans))):
        # if len(l) == m - 1:
        #     t += str(ans[_])
        #     if _ == len(ans) - 1:
        #         l.append(str(t)[::-1])
        #         t = ''
        # else:
            count += 1
            if count == 1:
                t += str(ans[_])
            elif count == 2:
                if ans[_] == '0':
                    if ans[_ + 2] == '0':
                        if ans[_ + 1] != '0':
                            t += str(ans[_])
                    else:
                        t += str(ans[_])
                else:
                    t += str(ans[_])
            elif count == 3:
                if ans[_] == '0':
                    if ans[_ + 1] != '0':
                        t += str(ans[_])
                else:
                    t += str(ans[_])
            elif count == 4 or _ == len(ans) - 1:
                if str(ans[_]) != '0':
                    t += str(ans[_])
                count = 0
                l.append(str(t)[::-1])
                t = ''
    return l[::-1]


a = ListNode(1)
b = ListNode(9999)
b1 = ListNode(9999)
b2 = ListNode(9999)
b3 = ListNode(9999)
b4 = ListNode(9999)
b5 = ListNode(9999)
b.next = b1
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5


print(addTwoHugeNumbers(a,b))