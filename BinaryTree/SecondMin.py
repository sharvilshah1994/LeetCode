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
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = []
        if not root.left and not root.right:
            return -1
        l = self.traverse(root, l)
        l.sort()
        return l[1]

    def traverse(self, root, l):
        if root:
            if root.data not in l:
                l.append(root.data)
            if not root.left and not root.right:
                return l
        if root.left and root.right:
            l1 = self.traverse(root.left, l)
            l2 = self.traverse(root.right, l)
            for _ in l2:
                if _ not in l1:
                    l1.append(_)
            return l1
        if root.left:
            return self.traverse(root.left, l)
        if root.right:
            return self.traverse(root.right, l)


print(Solution().findSecondMinimumValue(build_tree()))