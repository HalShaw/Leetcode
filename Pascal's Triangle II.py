class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for i in range(1, rowIndex+1):
            row = list(map(lambda x,y: x+y, [0]+row, row + [0]))
        return row
        '''
         Say we have the current layer [1, 2, 1]. 
         We then make 2 copies of this layer,
         add 0 to the start of one copy, 
         and add 0 to the end of one copy; 
         then we have [0, 1, 2, 1] and [1, 2, 1, 0]. 
         Then we can perform the element-wise add operation and we would have [1, 3, 3, 1]
        '''
         #输入6，结果：[1,6,15,20,15,6,1]        