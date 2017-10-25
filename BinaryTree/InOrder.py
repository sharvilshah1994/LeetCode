class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def build_tree():
    t = BinaryTreeNode(1)
    t1 = BinaryTreeNode(2)
    t2 = BinaryTreeNode(3)
    t3 = BinaryTreeNode(4)
    t4 = BinaryTreeNode(5)
    t.left = t1
    t.right = t2
    t1.left = t3
    t1.right = t4
    return t


class Solution(object):
    def in_order_traversal(self, tree):
        if tree:
            self.in_order_traversal(tree.left)
            print(tree.val)
            self.in_order_traversal(tree.right)


Solution().in_order_traversal(build_tree())