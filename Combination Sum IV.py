import itertools
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=[]
        res=[]
        for i in range(1,target+1):
            ls=list(itertools.combinations_with_replacement(nums,i))
            print(ls)
            for x in ls:
                if sum(list(x))==target:
                    l.append(x)
        print(l)
        for x in l:
            x=list(itertools.permutations(x,len(x)))
            res+=x
            print(res)
        return len(set(res))
if __name__ == '__main__':
    s=Solution()
    print(s.combinationSum4([1, 2, 3],5))
