class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lst=sorted(list(set(nums)))
        for i,x in enumerate(lst):
            if target<lst[0]:
                return 0
            elif x==target:
                return i
            elif target>lst[-1]:
                l=len(lst)
                return l
            else:
                while target<x:
                    target=x
                    return i
if __name__=='__main__':
    s=Solution()
    print(s.searchInsert([1,2,3,4,5,6,8],7))