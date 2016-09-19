class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=bin(n)
        b=a[2:]
        c=b.zfill(32)
        res=c[::-1]
        return int(res,2)

numbers of 1      
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn=bin(n)
        return str(bn).count('1')