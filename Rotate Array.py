class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k==0:
            return
        if k > len(nums):
            k = k%len(nums)
        if len(nums)==1:#长度为1，返回原数组
            nums=nums[:]
        nums[:]=nums[-k:]+nums[:len(nums)-k]