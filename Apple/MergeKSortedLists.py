class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_first_list():
    l = ListNode(1)
    l1 = ListNode(4)
    l2 = ListNode(5)
    l.next = l1
    l1.next = l2
    return l


def build_second_list():
    l = ListNode(2)
    l1 = ListNode(3)
    l2 = ListNode(6)
    l.next = l1
    l1.next = l2
    return l


def build_third_list():
    l = ListNode(2)
    l1 = ListNode(5)
    l.next = l1
    return l


class Solution(object):
    def mergeKLists(self, lists):
        curr = None
        for _ in lists:
            if not curr:
                curr = _
            else:
                curr = self.mergeTwoLists(curr, _)
        return curr

    def mergeTwoLists(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1 = build_first_list()
l2 = build_second_list()
l3 = build_third_list()
inp = Solution().mergeKLists([l1, l2, l3])


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(inp)
