import sys

class BinaryTreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def build_tree():
    t = BinaryTreeNode(10)
    t1 = BinaryTreeNode(29)
    t2 = BinaryTreeNode(309)
    t3 = BinaryTreeNode(40)
    t4 = BinaryTreeNode(5)
    t.left = t1
    t.right = t2
    t1.left = t3
    t1.right = t4
    return t


class Solution(object):
    def get_min_value(self, root):
        m = [sys.maxsize]
        if root:
            self.traverse(root, m)
        return m[0]

    def traverse(self, root, m):
        if root:
            m[0] = min(root.data, m[0])
        if root.left:
            self.traverse(root.left, m)
        if root.right:
            self.traverse(root.right, m)


print(Solution().get_min_value(build_tree()))