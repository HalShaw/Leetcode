class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers)<2:
            return None
        else:
            for i in range(len(numbers)):#自己写的，时间复杂度O(n^2)，AC不了
                for x in range(1,len(numbers)):
                    if numbers[i]+numbers[x]!=target:
                        continue
                    else:
                        if i==x:
                            return[i+1,x+1+1]
                        else:
                            return[i+1,x+1]
if __name__ == '__main__':
    s=Solution()
    print(s.twoSum([5,25,75],100))
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in xrange(len(numbers)):
            if i>0 and numbers[i-1]==numbers[i]:#跳过重复元素
                continue
            low=i+1
            high=len(numbers)-1
            while(low<=high):
                mid=(low+high)/2#二分法查找提速
                if target-numbers[i]==numbers[mid]:
                    return [i+1, mid+1]
                elif target-numbers[i]<numbers[mid]:
                    high=mid-1
                else:
                    low=mid+1