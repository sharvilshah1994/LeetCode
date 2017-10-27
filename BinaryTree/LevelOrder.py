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
    def level_order_traversal(self, root):
        if not root:
            return []
        ans = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            ans.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(ans)

Solution().level_order_traversal(build_tree())
