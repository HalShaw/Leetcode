import itertools
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ls=list(itertools.permutations(nums,len(nums)))
        for x in ls:
            x=list(x)
        return ls