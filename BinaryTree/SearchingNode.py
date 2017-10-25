class BinaryTreeNode(object):
    def __init__(self, x):
        self.data = x
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
    def search_for_x(self, root, x):
        if not root:
            return False
        if root.data == x:
            return True
        return self.search_for_x(root.left, x) or self.search_for_x(root.right, x)

print(Solution().search_for_x(build_tree(), 3))