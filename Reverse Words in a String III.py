class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ls=s.split(" ")
        lt=[]
        for x in ls:
            x=x[::-1]
            lt.append(x)
        return " ".join(lt)