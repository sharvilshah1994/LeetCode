class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def AverageLevels(root):
    return root.val
    
    pass

print(AverageLevels(TreeNode(3)))