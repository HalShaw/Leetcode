class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=nums[0]
        for i in range(1,len(nums)):
            a^=nums[i]#所有元素异或，相同的异或后为0,0与任何数异或都为它本身
        return a
    '''不使用异或,使用set
        s1 = set(nums)
        a2 = sum(s1)*2-sum(nums)
        return a2 ''' 
