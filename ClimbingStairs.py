class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        m, a, b = 0, 0, 1#Fibonacci数列,除了一二个，其余皆为前两个数之和
        while m < n:
            a, b = b, a + b
            m = m+1
        return b
        