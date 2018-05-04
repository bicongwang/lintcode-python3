"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: Whether it is a full tree
    """
    def isFullTree(self, root):
        if root.left and root.right:
            return self.isFullTree(root.left) and self.isFullTree(root.right)
        elif not root.left and not root.right:
            return True
        else:
            return False
