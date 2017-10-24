class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list():
    l = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l.next = l1
    l1.next = l2
    return l


class Solution(object):
    def reverse_linked_list(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev


inp = build_linked_list()
print_list_inp = Solution().reverse_linked_list(inp)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(print_list_inp)