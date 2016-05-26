class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """# 先排序，后比较
        l1=sorted([x for x in s.lower()])
        l2=sorted([y for y in t.lower()])
        s1="".join(l1)
        s2="".join(l2)
        if s1==s2:
            return True
        else:
            return False