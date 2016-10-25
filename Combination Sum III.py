import itertools
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        l=[]
        ls=list(itertools.combinations_with_replacement(range(1,10),k))
        for x in ls:
            if sum(x)==n and len(set(x))==len(x):#不能有重复元素
                l.append(list(x))
        return l
        '''
        Input: k = 3, n = 7
        Output: [[1,2,4]]
 		'''