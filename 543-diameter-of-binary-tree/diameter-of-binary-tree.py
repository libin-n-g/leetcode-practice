# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = []
        max_height_map = {}
        max_diameter = 0
        if root:
            stack.append((root, False))
        while stack:
            node, visited = stack.pop()
            if visited:
                if node.left is None:
                    left_height = 0
                else:
                    left_height = max_height_map[node.left]
                if node.right is None:
                    right_height = 0
                else:
                    right_height = max_height_map[node.right]
                max_diameter = max(max_diameter, right_height + left_height)
                max_height_map[node] = max(left_height, right_height) + 1
            else:
                stack.append((node, True))
                if node.left: stack.append((node.left, False))
                if node.right: stack.append((node.right, False))
        return max_diameter