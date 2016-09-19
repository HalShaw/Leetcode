class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ls=[]
        for x in range(12):#枚举所有可能，统计其中1的个数与输入的num比较
            for y in range(60):
                if (bin(x)+bin(y)).count('1')==num:
                    ls.append('%d:%02d'%(x,y))
        return ls
                    