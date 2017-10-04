class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def Init():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    return node1


def List2():
    node1 = ListNode(6)
    node2 = ListNode(7)
    node3 = ListNode(8)
    node1.next = node2
    node2.next = node3
    return node1


def MergeInBetween(a, b):
    l1 = Init()
    l2 = List2()
    le = 0
    current = l1
    while current:
        le += 1
        if le == (a-1):
            current.next = l2
            break
    new = Init()
    le = 0
    l3 = current
    while l3.next:
        l3 = l3.next
    while new:
        le += 1
        if le == b:
            l3.next = new.next
            break
        new = new.next
    while current:
        print(current.val)
        current = current.next

MergeInBetween(2, 4)

