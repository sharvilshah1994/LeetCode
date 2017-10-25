class BinaryTreeNode(object):
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def build_tree():
    queue = list()
    t = BinaryTreeNode(1)
    queue.append(t)
    t1 = BinaryTreeNode(2)
    t2 = BinaryTreeNode(3)
    t3 = BinaryTreeNode(4)
    t4 = BinaryTreeNode(5)
    t.left = t1
    t.right = t2
    t1.left = t3
    t1.right = t4
    return queue


class Solution(object):
    def level_order_traversal(self, queue):
        if not queue:
            return
        node = queue[0]
        print(node.data)
        queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        self.level_order_traversal(queue)


Solution().level_order_traversal(build_tree())