# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def check(left, right):
            if not left and not right:
                return True
            elif left is None and right is not None:
                return False
            elif right is None and left is not None:
                return False


            if left.val == right.val:
                return check(left.left, right.right) and check(left.right, right.left)
            else:
                return False
        return check(root.left, root.right)