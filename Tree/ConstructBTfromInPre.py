# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: vlr
        # inorder: lvr
        # i - inorder & p - preorder
        #preorser will tell me the curr tree where should grow
        # inorder will tell me left and right
        if not preorder  or not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        index_rt = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:index_rt])
        root.right = self.buildTree(preorder, inorder[index_rt+1:])

        return root
        
        
