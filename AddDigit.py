
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>9:
            c=0
            while num:
                c+=num%10
                num=num/10
            num=c
        return num
if __name__=='__main__':
    s=Solution()
    print s.addDigits(125)


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
        	return 0
        return (num-1)%9+1
if __name__=='__main__':
    s=Solution()
    print (s.addDigits(12))
            

