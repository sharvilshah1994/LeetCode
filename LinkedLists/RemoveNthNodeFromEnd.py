class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def Init():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    return node1


class Solution(object):
    """
    O(1): Space
    """
    def delete_n_from_end(self, head, n):
        head = self.reverse_list(head)
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        i = 1
        while curr and curr.next:
            if i == n:
                curr.next = curr.next.next
            else:
                curr = curr.next
            i += 1
        return self.reverse_list(dummy.next)

    def reverse_list(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def delete_n_from_end_Laveesh(self, head, d):
        n = k = head
        for i in range(d):
            k = k.next
        while k:
            n = n.next
            k = k.next
        return self.delete_node(head, n.val)

    def delete_node(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        curr = dummy
        while curr and curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


inp = Init()
print_list_inp = Solution().delete_n_from_end_Laveesh(inp, 3)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(print_list_inp)