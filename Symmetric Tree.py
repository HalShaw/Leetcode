# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isMirror(self,p,q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val: 
            return False
        else:
            return self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
