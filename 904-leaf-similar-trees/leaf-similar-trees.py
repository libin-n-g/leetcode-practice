# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_sequence(root):
            sequence = []
            stack = [root]
            while stack:
                curr_node = stack.pop()
                if curr_node.left:
                    stack.append(curr_node.left)
                if curr_node.right:
                    stack.append(curr_node.right)
                if not curr_node.left and not curr_node.right:
                    sequence.append(curr_node.val)
            return sequence
        sequence1 = get_sequence(root1)
        sequence2 = get_sequence(root2)
        if len(sequence1) != len(sequence2):
            return False 
        for i, j in zip(sequence1, sequence2):
            if i != j:
                return False
        return True