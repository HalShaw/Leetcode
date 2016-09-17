class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if not ransomNote:#为空
            return True
        if ransomNote in magazine:#字符串直接是子集，前面两个if可以去掉，但速度会慢10ms
            return True
        r=ransomNote
        m=magazine
        for x in r:
            if x in m and r.count(x)<=m.count(x):#r中的元素在m中出现且次数小于等于m中的，继续循环，完成后返回真，否则假
                continue
            else:
                return False
        return True
