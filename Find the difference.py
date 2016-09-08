class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:#需考虑三种情况，一是s为空，直接返回t
            return t
        else:
            ls=list(s)
            lst=list(t)
            for x in ls:
                for y in lst:
                    if x==y and ls.count(x)!=lst.count(y):#二是所以字母相同
                        return y
                    elif y in lst and y not in ls:#三是新加的字母不同于之前的
                        return list(set(lst)-set(ls))[0]
                