class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        a=0
        for x in nums:
            if x!=val:
                nums[a]=x #替换
                a+=1
        return a