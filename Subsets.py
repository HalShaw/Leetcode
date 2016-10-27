import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==[]:
            return [[]]
        else:
            l=[]
            res=[]
            for i in range(1,len(nums)+1):
                ls=list(itertools.combinations_with_replacement(nums,i))
                l+=ls
            for x in l:
                if len(set(x))==len(x):
                    res.append(x)
            return res+[[]]