import time
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        '''
        ls=[]
        for i in xrange(len(words)):
        	for j in xrange(i,len(words)):
        		if set(words[i])&set(words[j])==set([]):
        			s=len(words[i])*len(words[j])
        			ls.append(s)
        if ls==[]:
            return 0
        else:
            return max(ls)
        '''
        nums = []
        size = len(words)
        for w in words:
            nums += sum(1 << (ord(x) - ord('a')) for x in set(w)),#先把字符串数组转化成整数数组
        s = 0
        print nums
        for x in range(size):
            for y in range(size):
                if not (nums[x] & nums[y]):#相与不为真
                    s = max(len(words[x]) * len(words[y]), s)
        return s

if __name__ == '__main__':
	start=time.time()
	s=Solution()
	print s.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
	end=time.time()
	ti=end-start
	print ti