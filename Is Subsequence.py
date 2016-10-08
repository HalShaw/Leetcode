class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #简单版
        ls=list(s)
        for x in t:
            if ls and x==ls[0]:
                ls.pop(0)
        if ls:
            return False
        else:
            return True
        #高级版，函数all的应用
        t=iter(t)
        return all(c in t for c in s)