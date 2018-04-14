# LintCode in Python3 

Multiple solutions and comments are embedded in the code.     

Such as: 

```Python
# Solution 1: Simple 
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n+1):
            if i % 15 == 0:
                res.append('fizz buzz')
            elif i % 3 == 0:
                res.append('fizz')
            elif i % 5 == 0:
                res.append('buzz')
            else:
                res.append(str(i))
        return res


# Solution 2: Solve the challenge: "Can you do it with only one if statement?"
#
# Hint:
# 1. Python list comprehensions: [expr for iter_var in iterable if cond_expr]
# 2. short-circuit logic: (None or x) == x
class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        return [' '.join(([v for k, v in {3: 'fizz', 5: 'buzz'}.items() if i % k == 0])) or str(i) for i in range(1, n+1)]

```