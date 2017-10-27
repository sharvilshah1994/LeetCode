class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def Init():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    return node1

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(-1)
        pre, pre.next = prev, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return prev.next

head = Solution().swapPairs(Init())
while head:
    print(head.val)
    head = head.next



