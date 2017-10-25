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
    def delete_n_from_end(self, head, n):
        dic = {}
        count = 0
        while head:
            dic[count] = head.val
            head = head.next
            count += 1
        m = len(dic)
        prev = ListNode(-1)
        curr = prev
        for k in dic:
            if k != (m - n):
                l = ListNode(dic[k])
                curr.next = l
                curr = curr.next
        return prev.next


inp = Init()
print_list_inp = Solution().delete_n_from_end(inp, 2)


def traverse_list(head):
    while head:
        print(head.val)
        head = head.next


traverse_list(print_list_inp)