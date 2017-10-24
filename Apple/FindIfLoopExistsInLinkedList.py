class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list():
    l = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l2
    return l


class Solution(object):
    def check_if_loop_exists(self, head):
        slow = head
        fast = head
        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


inp = build_linked_list()
print(Solution().check_if_loop_exists(inp))