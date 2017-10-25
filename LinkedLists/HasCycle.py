class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def build_linked_list():
    l = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l3 = ListNode(4)
    l4 = ListNode(5)
    l.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l
    return l


class Solution(object):
    def has_cycle(self, head):
        try:
            slow = fast = head
            while head:
                slow = slow.next
                fast = fast.next.next
                if slow.val == fast.val:
                    return True
        except:
            return False


print(Solution().has_cycle(build_linked_list()))