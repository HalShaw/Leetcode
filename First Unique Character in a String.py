from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=Counter(s)#使用计数函数，生成字典
        if not s:
            return -1
        elif [x for x in l.values() if x==1]==[]:#如果没有只出现一次字符
            return -1
        else:    
            for x in s:
                if l.get(x)==1:#返回第一个出现一次的索引
                    return s.index(x)
