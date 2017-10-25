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


def printList(val, prev):
    while prev:
        print("Val is "+str(val) + " val in prev "+ str(prev.val))
        prev = prev.next


def DeleteNodesGreaterThanX(n):
    head = Init()
    prev = ListNode(None)
    current = head
    while current:
        if current.val > n and not prev:
            head = head.next
        elif current.val > n and prev:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    while head:
        print(head.val)
        head = head.next

DeleteNodesGreaterThanX(2)
