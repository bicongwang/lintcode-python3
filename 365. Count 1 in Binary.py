# Solution 1: Simple 
# 
# Time complexity: O(n), n=32 in this problem
# Hint: 00001100 & 00000001 == 0, 00001100 & 00001000 > 0
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        x = 1
        count = 0
        for i in range(32):
            if num & x != 0:
                count += 1
            x = x << 1
        return count 


# Solution 2: Solve the challenge: 
# "If the integer is n bits with m 1 bits. Can you do it in O(m) time?"
# 
# Time complexity: O(m), m is the number of 1-bits
# Hint: 
# 1. Integer and bit operation in python is different from java, so we must check if num < 0.
# 2. 00011000 & 00010111 == 00010000 (00011000 - 1 == 00010111)
class Solution:
    """
    @param: num: An integer
    @return: An integer
    """
    def countOnes(self, num):
        # write your code here
        if num >= 0:
            count = 0
        else:
            num = 2 ** 31 + num # then num is a positive or 0, not a negative.
            count = 1
        while num != 0:
            count += 1
            num = num & (num - 1)
        return count 
