# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([(root, 0)])
        average = []
        while queue:
            level_sum = 0
            level_count = 0
            for _ in range(len(queue)):
                node, level = queue.popleft()
                if node.left: queue.append((node.left, level + 1))
                if node.right: queue.append((node.right, level + 1))
                level_sum += node.val
                level_count += 1
            average.append(level_sum/level_count)
        return average