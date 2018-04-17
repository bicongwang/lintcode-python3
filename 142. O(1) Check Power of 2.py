# Solution 1: Solve the challenge: 'O(1) time'
# 
# Hint: Power of 2 is 00000001, 00000010, 00000100, ···
#       if n & (n - 1) is 0, it is power of 2 except 0
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        return bool(n) and not bool(n & (n - 1))
