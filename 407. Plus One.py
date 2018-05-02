# Solution1: 
#   No more to say!
class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        i = len(digits) - 1
        while i > -1:
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if not i:
                    digits.insert(0, 1)
                i -= 1
        return digits
