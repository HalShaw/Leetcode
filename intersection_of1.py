class Solution(object):
    def intersection(self,nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1=[]
        l2=[]
        for x in nums1:
            for y in nums2:
                if x==y:
                    t=x
                    l1.append(t)
                    l2=list(set(l1))
        return l2
if __name__=='__main__':
    s=Solution()
    nums1=[1,2,2,3]
    nums2=[2,5,8]
    print s.intersection(nums1, nums2)
