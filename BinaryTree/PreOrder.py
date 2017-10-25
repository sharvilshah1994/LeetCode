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
    def pre_order_traversal(self, tree):
        if tree:
            print(tree.val)
            self.pre_order_traversal(tree.left)
            self.pre_order_traversal(tree.right)


Solution().pre_order_traversal(build_tree())