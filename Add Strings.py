from itertools import izip_longest
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res, c = "", 0
        for (x, y) in izip_longest(num1[::-1], num2[::-1], fillvalue='0'):#把两个数字从最低位同时迭代出来，不够用0补
            s = (int(x) + int(y) + c)#对应位数相加
            d, c = s % 10, int(s / 10)#如果结果超过10，取余，c为进位的数
            res = str(d) + res
        
        if c > 0: #最后如果有进位，再把c放在最前面
            res = str(c) + res

        return res