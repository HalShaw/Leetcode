class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        
        c=0
        for x in xrange(10**n):
            if len(set(str(x)))!=len(str(x)):
                c+=1
        return 10**n-c
        """
        l=[1,9,9,8,7,6,5,4,3,2,1]
        #先算积再算和，l很重要
        return reduce(lambda x,y:x+y,[reduce(lambda x,y:x*y,l[:i+1]) for i in range(n+1)])