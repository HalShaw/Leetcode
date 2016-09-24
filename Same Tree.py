# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p==q==None:
            return True
        elif p==None or q==None:
            return False
        elif p.val!=q.val:
            return False
        return self.isSameTree(q.right,p.right) and self.isSameTree(q.left,p.left)
            