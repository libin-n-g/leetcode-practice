# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node:
                curr_node.right, curr_node.left = curr_node.left, curr_node.right
                stack.append(curr_node.right)
                stack.append(curr_node.left)
        return root