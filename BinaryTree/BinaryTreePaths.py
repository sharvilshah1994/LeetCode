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
            stack_l = [(root.left, [root.left])]
            stack_r = [(root.right,[root.right])]
            s_l = self.get_path_with_dfs(stack_l, end)
            if s_l:
                return [root] + s_l
            else:
                return [root] + self.get_path_with_dfs(stack_r, end)
        else:
            self.get_path_binary_tree(root.left, start, end)
            self.get_path_binary_tree(root.right, start, end)

    def get_path_with_dfs(self, stack, end):
        while stack:
            (vertex, path) = stack.pop()
            for nxt in path:
                if nxt.data == end:
                    return path
                else:
                    if vertex.left:
                        stack.append((nxt, path + [vertex.left]))
                    if vertex.right:
                        stack.append((nxt, path + [vertex.right]))
        return []


for _ in (Solution().get_path_binary_tree(build_tree(), 1, 4)):
    print(_.data)
