class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

le = 0
while node1:
    le += 1
    node1 = node1.next
print(le)