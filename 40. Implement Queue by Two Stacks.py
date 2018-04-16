# Solution 1:  
# 
# Comment: push(): push element to self._stack1
#          pop(): pop element from self._stack2
#          it will adjust stack when we invoke pop()
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self._stack1 = []
        self._stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self._stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if self._adjust_stack():
            return self._stack2.pop()
        
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if self._adjust_stack():
            return self._stack2[-1]
        
    def _adjust_stack(self):
        if not self._stack2:
            while self._stack1:
                self._stack2.append(self._stack1.pop(-1))
        return bool(self._stack2)
