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
    def check_if_left_right_symm(self, root):
        def is_symm(l, r):
            if not l and not r: return True
            if l and r and l.data == r.data:
                return is_symm(l.left, r.right) and is_symm(l.right, r.left)
            return False
        return is_symm(root, root)


print(Solution().check_if_left_right_symm(root=build_tree()))