import sys


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
    def get_width(self, root):
        if not root:
            return []
        ans = []
        level = [root]
        while level:
            l = []
            for i in level:
                if i:
                    l.append(i.data)
                else:
                    l.append(None)
            ans.append(l)
            temp = []
            for node in level:
                if node:
                    temp.extend([node.left, node.right])
            level = [leaf for leaf in temp]
        m = -sys.maxsize
        for _ in ans:
            m = max(m, len(_))
        print(m)


Solution().get_width(build_tree())