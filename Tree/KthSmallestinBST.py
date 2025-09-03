# Given the root of a binary search tree, and an integer k, 
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #print(root.val)
        min1 = float("inf")
        count = [k]
        ans = [0]
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            if count[0] == 1:
                ans[0] = root.val 
            count[0]-=1
            if count[0] > 0:
                dfs(root.right)
        dfs(root)
        return ans[0]
            

