# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            if not root.left and not root.right:
                return 0
            else:
                result = 0
                if root.left:
                    result += self.traverse(root.left, True)
                if root.right:
                    result += self.traverse(root.right, False)
                return result
    def traverse(self, root, isLeft):
        if not root.left and not root.right:
            if isLeft:
                return root.val
            else:
                return 0
        else:
            result = 0
            if root.left:
                result += self.traverse(root.left, True)
            if root.right:
                result += self.traverse(root.right, False)
            return result       
            