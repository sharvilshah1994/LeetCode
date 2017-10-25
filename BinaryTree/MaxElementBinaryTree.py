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
    def max_item_tree(self, root):
        max_value = -1
        if root:
            left = self.max_item_tree(root.left)
            right = self.max_item_tree(root.right)
            if left > right:
                max_value = left
            else:
                max_value = right
            if root.data > max_value:
                max_value = root.data
        return max_value


print(Solution().max_item_tree(build_tree()))