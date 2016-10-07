class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        递归公式
        f(0) = nums[0]
		f(1) = max(num[0], num[1])
		f(k) = max( f(k-2) + nums[k], f(k-1) )
        """
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now
        