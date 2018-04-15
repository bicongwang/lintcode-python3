# Solution 1: Simple 
# 
# Hint: https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class Solution:
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

# Solution 2: Solve the challenge: 
# "If we call getInstance concurrently, can you make sure your code could run correctly?"
# 
# Hint: threading.Lock()
import threading

class Solution:
    _lock = threading.Lock()
    
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        cls._lock.acquire()
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        cls._lock.release()
        return cls._instance
