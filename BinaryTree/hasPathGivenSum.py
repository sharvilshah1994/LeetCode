class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def build_tree():
    # t = TreeNode(4)
    # t1 = TreeNode(1)
    # t2 = TreeNode(-2)
    # t3 = TreeNode(3)
    # t4 = TreeNode(3)
    # t5 = TreeNode(1)
    # t6 = TreeNode(2)
    # t7 = TreeNode(-2)
    # t8 = TreeNode(-3)
    # t.left = t1
    # t1.left = t2
    # t2.right = t3
    # t.right = t4
    # t4.left = t5
    # t4.right = t6
    # t6.left = t7
    # t6.right = t8
    t = TreeNode(-1000)
    t1 = TreeNode(-1000)
    t2 = TreeNode(-1000)
    t3 = TreeNode(-1000)
    t.left = t1
    t1.right = t2
    t2.left = t3
    return t


def hasPathWithGivenSum(t, s):
    if not t and s == 0:
        return True
    sum = 0
    if t:
        sum += t.value
        if t.left:
            if dfs(t.left, s, sum):
                return True
        if t.right:
            if dfs(t.right, s, sum):
                return True
        if not t.left and not t.right:
            if sum == s:
                return True
    return False

def dfs(t, s, sum):
    if t:
        sum += t.value
        if not t.left and not t.right:
            print(sum)
            if sum == s:
                return True
    if t.left and t.right:
        return dfs(t.left, s, sum) or dfs(t.right, s, sum)
    if t.left:
        return dfs(t.left, s, sum)
    if t.right:
        return dfs(t.right, s, sum)

print(hasPathWithGivenSum(build_tree(), -4000))