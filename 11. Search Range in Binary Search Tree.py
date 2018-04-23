"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Solution 1: Inorder traversal (Recursion)
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = list()
        if root:
            if root.val >= k1:
                result.extend(self.searchRange(root.left, k1, k2))
            if k1 <= root.val <= k2:
                result.append(root.val)
            if root.val <= k2:
                result.extend(self.searchRange(root.right, k1, k2))
        return result 


# Solution 2: Inorder traversal (Without recursion)
class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        result = list()
        stack = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                if root and root.val < k1:
                    root.left = None
            if not root:
                top = stack.pop()
                if k1 <= top.val <= k2:
                    result.append(top.val)
                if top.val > k2:
                    top.right = None
                root = top.right
        return result
