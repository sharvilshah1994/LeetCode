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


def InsertAtBeginning(n):
    new = ListNode(n)
    head = Init()
    new.next = head
    while new:
        print(new.val)
        new = new.next


def InsertAtEnd(n):
    new = ListNode(n)
    head = Init()
    if head is None:
        return new
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new
    while head:
        print(head.val)
        head = head.next


def InsertInMiddle(n, position):
    new = ListNode(n)
    le = 0
    head = Init()
    current = head
    while current:
        le += 1
        if le == (position-1):
            new.next = current.next
            current.next = new
            break
        current = current.next
    while head:
        print(head.val)
        head = head.next


# InsertAtBeginning(0)
# InsertAtEnd(4)
InsertInMiddle(5, 2)
