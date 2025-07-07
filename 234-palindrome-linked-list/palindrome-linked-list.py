# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []  # Stack to store node values
        curr_node = head
        
        # Step 1: Traverse the list and push all node values onto the stack
        while curr_node:
            stack.append(curr_node.val)
            curr_node = curr_node.next
        
        # Step 2: Reset curr_node to head for second traversal
        curr_node = head
        
        # Step 3: Compare each node value with values popped from stack (reverse order)
        while stack and curr_node:
            if curr_node.val != stack.pop():
                return False  # Mismatch means not a palindrome
            curr_node = curr_node.next
        
        # Step 4: Ensure both stack and list are fully traversed
        if stack or curr_node:
            return False  # Leftover nodes or stack elements mean unequal lengths
        else:
            return True  # All values matched, list is a palindrome

            