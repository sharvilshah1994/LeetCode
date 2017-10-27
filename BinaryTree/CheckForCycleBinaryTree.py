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
    def check_for_cycle(self, root):
        if root:
            visited = set()
            return self.check_helper(root, visited)
        return False

    def check_helper(self, root, visited):
        if root not in visited:
            visited.add(root)
            if not root.left and not root.right:
                return False
        else:
            return True
        if root.left and root.right:
            return self.check_helper(root.left, visited) or self.check_helper(root.right, visited)
        elif root.left:
            return self.check_helper(root.left, visited)
        elif root.right:
            return self.check_helper(root.right, visited)

print(Solution().check_for_cycle(build_tree()))
