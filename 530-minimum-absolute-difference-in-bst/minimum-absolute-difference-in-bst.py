# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = float('inf')  # Initialize minimum difference to infinity
        stack = []  # Stack for iterative in-order traversal
        prev_val = float('-inf')  # Store the previous node's value (start with negative infinity)
        node = root  # Start at the root
        
        # Continue while there are nodes to process (either current node or stack is non-empty)
        while node or stack:
            # Traverse as far left as possible, pushing nodes onto the stack
            if node:
                stack.append(node)
                node = node.left
            else:
                # Pop the next node (smallest remaining value in current subtree)
                node = stack.pop()
                # Calculate difference between current node and previous node
                min_diff = min(min_diff, node.val - prev_val)
                # Update previous value to current node's value
                prev_val = node.val
                # Move to the right subtree
                node = node.right
        
        return min_diff  # Return the smallest difference found
# Example usage with the given tree:
#       236
#      /   \
#    104    701
#     /       \
#   NULL 227   NULL 911
#
# Input: root = [236,104,701,null,227,null,911]
# Output: 11
# Explanation:
# - In-order traversal of the BST visits nodes in ascending order: [104, 227, 236, 701, 911]