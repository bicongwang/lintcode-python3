"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Solution1: No more to say.
class Solution:
    """
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        if inorder and postorder:
            middle = TreeNode(postorder[-1])
            index = inorder.index(postorder[-1])
            middle.left = self.buildTree(inorder[:index], postorder[:index])
            middle.right = self.buildTree(inorder[index+1:], postorder[index:-1])
            return middle
