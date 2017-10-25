class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def Init():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    return node1


class Solution(object):
    def check_for_pallindrome(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        if l == l[::-1]:
            return True
        return False

print(Solution().check_for_pallindrome(Init()))