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
    def get_path_binary_tree(self, root, start, end):
        if root.data == start:
            stack = [(root, [root])]
            s = self.binary_tree_path_helper(stack, end)
            if s:
                return s
            return -1
        else:
            self.get_path_binary_tree(root.left, start, end)
            self.get_path_binary_tree(root.right, start, end)

    def binary_tree_path_helper(self, stack, end):
        while stack:
            (vertex, path) = stack.pop()
            for nxt in path:
                if nxt.data == end:
                    return path
                else:
                    if nxt.left:
                        stack.append((nxt.left, path + [nxt.left]))
                    elif nxt.right:
                        stack.append((nxt.right, path + [nxt.right]))


for _ in (Solution().get_path_binary_tree(build_tree(), 1, 4)):
    print(_.data)


# print(Solution().get_path_binary_tree(build_tree(),1, 4))