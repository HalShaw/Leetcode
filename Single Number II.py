class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = set(nums)
        a2 = sum(s1)*3-sum(nums)
        return a2/2        