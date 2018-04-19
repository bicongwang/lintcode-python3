# Solution 1: Dynamic Programming
# 
# like problem: 109. Triangle
# The minimum path sum‘s recursion formula:
#   1. the top left : self
#   2. the top other: left + self
#   3. the left other: top + self
#   3. the other: min(left's value, top's value) + self
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        for i in range(0, len(grid)):
            for j in range(len(grid[i])):
                if not i and not j:
                    pass
                elif not i:
                    grid[i][j] += grid[i][j-1]
                elif not j:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]
