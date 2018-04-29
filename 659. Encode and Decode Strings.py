# Solution:
#    Encode: length#string
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return ''.join(map(lambda s: str(len(s))+'#'+s, strs))

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        strs = []
        start = end = 0
        while start < len(str):
            if str[end] != '#':
                end += 1
            else:
                length = int(str[start:end])
                strs.append(str[end+1:end+length+1])
                start = end = end+length+1
        return strs
