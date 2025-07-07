# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = []
        if root:
            stack.append((root, targetSum - root.val))
        while stack:
            node, target_sum = stack.pop()
            if not node.left and not node.right and target_sum == 0:
                return True
            if node.left: stack.append((node.left, target_sum - node.left.val))
            if node.right: stack.append((node.right, target_sum - node.right.val))
        return False