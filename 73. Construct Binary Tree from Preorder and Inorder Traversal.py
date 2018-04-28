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
    @param preorder: A list of integers that preorder traversal of a tree
    @param inorder: A list of integers that inorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if inorder and preorder:
            middle = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            middle.left = self.buildTree(preorder[1:index+1], inorder[:index])
            middle.right = self.buildTree(preorder[index+1:], inorder[index+1:])
            return middle
