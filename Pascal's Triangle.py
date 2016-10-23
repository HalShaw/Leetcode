class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for _ in range(2, numRows):#控制循环
            last = res[-1]#每次取上一个结果里的最后一个list
            temp = []
            for i in range(len(last)-1):
                temp.append( last[i]+last[i+1] )#新list里的元素等于上两个元素的和
            temp = [1] + temp + [1]
            res.append( temp )
        return res   
        #输出结果：[[1],[1,1],[1,2,1]] 
        #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1],[1,5,10,10,5,1]]

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #另一种解法，更快更简洁
        l=[]
        if numRows==0:
            return []
        else:
            row = [1]
            for i in range(1, numRows+1):
                l.append(row)
                row = list(map(lambda x,y: x+y, [0]+row, row + [0]))
            return l         