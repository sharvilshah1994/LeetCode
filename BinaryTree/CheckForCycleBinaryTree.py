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
        visited = set()
        stack = [root]
        if self.dfs(visited, stack):
            return True
        return False

    def dfs(self, visited, stack):
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                if vertex.left:
                    stack.append(vertex.left)
                if vertex.right:
                    stack.append(vertex.right)
            else:
                return False
        return True


print(Solution().check_for_cycle(build_tree()))
