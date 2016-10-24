class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return []
        elif len(set(nums))==1:
            return nums[0]
        elif len(set(nums))==2:
            return max(nums)
        else:
            nums=sorted(list(set(nums)))
            return nums[-3]