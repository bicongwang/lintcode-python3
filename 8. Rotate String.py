# Solution 1: Solve the challenge: 
# 'Rotate in-place with O(1) extra memory.'
# 
# Hint: rotate three times
class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if str and offset:
            offset %= len(str)
            self._rotate(str, 0, len(str)-1)
            self._rotate(str, 0, offset-1)
            self._rotate(str, offset, len(str)-1)
        
    def _rotate(self, str, start, end):
        while start < end:
            str[start], str[end] = str[end], str[start]
            start += 1
            end -= 1
