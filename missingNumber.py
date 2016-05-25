class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[x for x in range(max(nums)+1)]
        if len(l)==len(nums):
            return len(nums)
        else:
            a=list(set(l)-set(nums))
            return int(a[0])