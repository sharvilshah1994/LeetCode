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


def DeleteFirstNode():
    head = Init()
    while head:
        head = head.next
        break
    while head:
        print(head.val)
        head = head.next

def DeleteLastNode():
    head = Init()
    current = head
    while current:
        if current.next.next is None:
            current.next = None
            break
        current = current.next
    while head:
        print(head.val)
        head = head.next

def DeleteNode(n):
    head = Init()
    current = head
    while current:
        if current.next.val == n:
            current.next = current.next.next
            break
        current = current.next
    while head:
        print(head.val)
        head = head.next

# DeleteFirstNode()
# DeleteLastNode()
DeleteNode(2)