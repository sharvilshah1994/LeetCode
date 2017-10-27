class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def Init():
    node1 = ListNode(3)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node1.next = node2
    node2.next = node3
    return node1


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        return self.mergeList(self.sortList(head), self.sortList(slow))

    def mergeList(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeList(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeList(l1, l2.next)
            return l2


l = Solution().sortList(Init())
while l:
    print(l.val)
    l = l.next

list()