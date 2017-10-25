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
    def insert_element(self, root, x):
        if not root:
            root = BinaryTreeNode(x)
        else:
            self.insert_helper(root, x)
        return root

    def insert_helper(self, root, x):
        if not root.left:
            root.left = BinaryTreeNode(x)
        else:
            if not root.right:
                root.right = BinaryTreeNode(x)
            else:
                self.insert_helper(root.left, x)


t = Solution().insert_element(build_tree(), 7)
t = Solution().insert_element(t, 8)
t = Solution().insert_element(t, 9)


def print_elems(t):
    if t:
        print(t.data)
        print_elems(t.left)
        print_elems(t.right)

print_elems(t)