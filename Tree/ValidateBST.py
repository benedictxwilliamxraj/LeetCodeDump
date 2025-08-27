# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low, high):
            if node is None:
                return True
            
            if (low >= node.val or  high<= node.val):
                return False
            
        
            return check(node.right, node.val, high) and check(node.left, low, node.val)

        
        return check(root, float('-inf'), float('inf'))