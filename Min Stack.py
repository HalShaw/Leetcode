class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.lst.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        self.lst.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.lst is not None:
            return self.lst[len(self.lst)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.lst) == 0:
            return None
        else:
            return self.lst[len(self.lst) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()