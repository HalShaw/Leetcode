import itertools
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ls=list(itertools.combinations(range(1,n+1), k))
        for x in ls:
            x=list(x)
        return ls