class Solution(object):
    def intToRoman(self, num):
        """
        数字到罗马数字的转换
        :type num: int
        :rtype: str
        """
        dic = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]#两个数组，从高到低
        res = ""
        for st, n in zip(dic, nums):#zip函数同时调用两个数组
            res += st * int(num / n)#计算num中含有多少个字母，从高到低
            num %= n#取余降低一位后继续计算
        return res        