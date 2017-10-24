def MergeTwoLists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = MergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = MergeTwoLists(l1, l2.next)
        return l2


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


head = MergeTwoLists(Init(), Init())
while head:
    print(head.val)
    head = head.next
