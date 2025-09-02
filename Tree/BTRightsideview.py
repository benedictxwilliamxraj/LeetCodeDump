# Given the root of a binary tree, imagine yourself standing on the right side of it, r
# eturn the values of the nodes you can see ordered from top to bottom.

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #bfs
        if not root: 
            return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i+1 == n:
                    res.append(node.val)
        return res
