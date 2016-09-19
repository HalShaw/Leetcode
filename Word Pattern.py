class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        s=pattern
        t=str.split()
        return map(s.index, s) == map(t.index, t)
        
            