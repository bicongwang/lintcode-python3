# Solution 1: Simple 
# 
# Comment: You have no need to use array which will cause a larger space complexity
# Space complexity: O(1)
# Time complexity: O(n)
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        i_1, i_2 = 0, 1
        for i in range(n-1):
            i_1, i_2 = i_2, i_1 + i_2
        return i_1