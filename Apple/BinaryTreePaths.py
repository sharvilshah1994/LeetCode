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
    def binary_tree_path(self, root):
        ans = list()
        if not root:
            return ans
        self.dfs(root, "", ans)
        return ans

    def dfs(self, root, pre, ans):
        if not root.left and not root.right:
            ans.append(pre + str(root.val))
        if root.left:
            self.dfs(root.left, pre + str(root.val) + "->", ans)
        if root.right:
            self.dfs(root.right, pre + str(root.val) + "->", ans)


print(Solution().binary_tree_path(build_tree()))
