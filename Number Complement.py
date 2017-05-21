class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b_num=bin(num)[2:]
        c_num=""
        for x in b_num:
            if x == '1':
                c_num+='0'
            elif x == '0':
                c_num+='1'
        return int(c_num,2)