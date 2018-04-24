# Solution 1: Simple 
# 
# Time complexity: O(n)
class Solution:
    """
    @param: string: An array of Char
    @param: length: The true length of the string
    @return: The true length of new string
    """
    def replaceBlank(self, string, length):
        # write your code here
        c = string.count(' ') if string else 0
        j = length + 2 * c - 1
        for i in range(length-1, -1, -1):
            if string[i] != ' ':
                string[j] = string[i]
                j -= 1
            else:
                string[j-2:j+1] = '%20'
                j -= 3
        return length + 2 * c
        