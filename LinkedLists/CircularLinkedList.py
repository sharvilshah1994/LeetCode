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
    def get_count_nodes(self, head):
        print(head.val)
        val = head.next
        while val != head:
            print(val.val)
            val = val.next


inp = build_linked_list()
Solution().get_count_nodes(inp)
