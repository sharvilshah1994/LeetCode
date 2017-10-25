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
    def delete_nodes_greater_k(self, head, k):
        prev = ListNode(None)
        curr = head
        while curr:
            if curr.val > k and not prev:
                curr = curr.next
            elif curr.val > k and prev:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head


inp = build_linked_list()
ans = Solution().delete_nodes_greater_k(inp, 2)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(ans)