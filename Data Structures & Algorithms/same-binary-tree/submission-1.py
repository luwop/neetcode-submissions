# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p, q]

        while stack:
            lf1, lf2 = stack.pop(), stack.pop()

            if not lf1 and not lf2:
                continue
            if not lf1 or not lf2:
                return False
            if lf1.val != lf2.val:
                return False
            
            stack.append(lf1.left)
            stack.append(lf2.left)
            stack.append(lf1.right)
            stack.append(lf2.right)
        
        return True
        