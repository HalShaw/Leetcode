class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.index,s)==map(t.index,t)#相同格式都可以用
        
