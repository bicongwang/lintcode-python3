"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        # write your code here
        if start <= end:
            tree_node = SegmentTreeNode(start, end)
            if start < end:
                tree_node.left = self.build(start, (start+end)//2)
                tree_node.right = self.build((start+end)//2+1, end)
            return tree_node
