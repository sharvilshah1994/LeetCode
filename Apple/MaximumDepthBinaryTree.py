class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Init():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    return node1


def MaxDepth(root):
    if root:
        return 1 + max(MaxDepth(root.left), MaxDepth(root.right))
    else:
        return 0


t = Init()
print(MaxDepth(t))
