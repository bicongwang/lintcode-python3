# Solution 1: Solve the challenge: 
# "Reverse it in-place and in one-pass"
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        head = ListNode(0, next=head)
        node = head.next
        while node and node.next:
            temp = node.next
            node.next = node.next.next
            temp.next = head.next
            head.next = temp
        return head.next
