class Solution(object):
    def int2str(self,num):
        return str(num)
    def str2int(self,st):
        return int(st)
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=map(self.int2str,digits)#整数列表转为字符串列表
        nums=str(int(''.join(digits))+1)#字符串转整数加1
        nums=[x for x in nums]#生成每一位字符串对应的字符
        return map(self.str2int,nums)#转每一位字符为整数
