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
    def delete_node(self, head, target):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


inp = build_linked_list()
ans = Solution().delete_node(inp, 2)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(ans)
