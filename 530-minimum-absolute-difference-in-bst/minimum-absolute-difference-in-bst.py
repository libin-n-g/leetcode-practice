# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')
        stack = []
        prev_val = float('-inf')
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                min_diff = min(min_diff, node.val - prev_val)
                prev_val = node.val
                node = node.right
        return min_diff
#       236
#    104    701
# NULL 227  NULL 911 