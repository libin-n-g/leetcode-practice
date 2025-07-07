# Reverses a portion of a singly-linked list from position 'left' to 'right' (1-indexed).
# The algorithm uses a dummy node to handle edge cases (e.g., when left=1).
# It iterates to the node before the reversal section, then reverses the links within
# the specified range, and finally reconnects the reversed section to the rest of the list.
# Time complexity: O(n), where n is the length of the linked list.
# Space complexity: O(1), as it uses a constant amount of extra space.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (e.g., reversing from head)
        dummy_node = ListNode(float('-inf'))
        dummy_node.next = head
        curr_node = dummy_node
        
        # Move to the node just before the reversal section (left-1 position)
        for _ in range(left):
            left_node, curr_node = curr_node, curr_node.next
            # left_node is the node before the reversal section
            # curr_node is at position 'left'
        
        # Reverse the section from 'left' to 'right'
        prev_node = None
        for _ in range(right - left + 1):
            # Store the next node
            next_node = curr_node.next
            # Reverse the link
            curr_node.next = prev_node
            # Move pointers forward
            prev_node, curr_node = curr_node, next_node
            # After loop, curr_node is one position after 'right'
            # prev_node is the new head of the reversed section
        
        # Reconnect the reversed section to the rest of the list
        left_node.next.next = curr_node  # Connect the end of reversed section to the node after 'right'
        left_node.next = prev_node       # Connect the node before 'left' to the new head of reversed section
        
        # Return the head of the modified list
        return dummy_node.next

# Example usage:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Explanation:
# - Original list: 1 -> 2 -> 3 -> 4 -> 5
# - left=2, right=4 means reverse the sublist [2,3,4]
# - Step-by-step:
#   1. Dummy node points to head: dummy -> 1 -> 2 -> 3 -> 4 -> 5
#   2. Move to left-1 (node 1): left_node = 1, curr_node = 2
#   3. Reverse [2,3,4]:
#      - First iteration: 2 -> None, prev_node = 2, curr_node = 3
#      - Second iteration: 3 -> 2, prev_node = 3, curr_node = 4
#      - Third iteration: 4 -> 3, prev_node = 4, curr_node = 5
#   4. Reconnect:
#      - left_node.next (1.next) = prev_node (4), so 1 -> 4
#      - left_node.next.next (4.next) = curr_node (5), so 4 -> 5
#   5. Resulting list: 1 -> 4 -> 3 -> 2 -> 5
# - The sublist [2,3,4] is reversed to [4,3,2], and the list is reconnected properly.
        