# Solution 1: Dynamic Programming
# 
# The minimum path sum‘s recursion formula:
#   1. the first floor: self
#   2. the edge of triangle (only one parent): the parent's value + self
#   3. the center of triangle (two parents): minimum of two parents' value + self
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if not j:
                    triangle[i][j] += triangle[i-1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] += triangle[i-1][-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
