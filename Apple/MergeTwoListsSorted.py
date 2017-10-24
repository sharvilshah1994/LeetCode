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


class Solution(object):
    def merge_sort(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge_sort(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_sort(l1, l2.next)
            return l2

l1 = build_first_list()
l2 = build_second_list()
inp = Solution().merge_sort(l1, l2)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(inp)
