# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            found = False
            node, level = queue.popleft()
            if node.left: 
                queue.append((node.left, level+1))
                found = True
            if node.right: 
                queue.append((node.right, level+1))
                found = True
            if not found:
                return level