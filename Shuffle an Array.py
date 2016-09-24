from random import shuffle#自带洗牌方法
from copy import deepcopy
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.nums=nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums=deepcopy(self.nums)#导入deepcopy来拷贝引用对象，不然直接用的话会影响reset的输出
        shuffle(nums)
        return nums
