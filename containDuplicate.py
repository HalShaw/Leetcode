class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(len(nums)-len(list(set(nums)))>0):
            return True
        elif len(nums)==1:
            return False
        else:
            return False
       