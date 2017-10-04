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
    dummy = ListNode(-1)
    dummy.next = head
    next = dummy

    while next != None and next.next != None:
        if next.next.val == n:
            next.next = next.next.next
        else:
            next = next.next
    dummy = dummy.next
    while dummy:
        print(dummy.val)
        dummy = dummy.next

DeleteFirstNode()
DeleteLastNode()
DeleteNode(1)