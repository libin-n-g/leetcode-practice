# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if not q_node and not p_node:
                continue
            elif None in [q_node, p_node] or q_node.val != p_node.val:
                return False
            stack.append((q_node.left, p_node.left))
            stack.append((q_node.right, p_node.right))
        return True