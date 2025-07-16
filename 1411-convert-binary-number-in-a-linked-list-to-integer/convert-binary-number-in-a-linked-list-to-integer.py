# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Initialize the value of the head node (most significant bit, 0 or 1)
        num = head.val
        
        # Traverse the linked list until the last node
        while head.next:
            # Multiply the current number by 2 to shift left, accounting for the next bit’s positional value
            # This mimics the binary-to-decimal conversion process 
            # 01 -> 010
            num = num << 1
            # Move to the next node in the list
            head = head.next
            # Add/ Do OR the value of the current node (0 or 1) to the number
            # 010 | 001 = 011 or 010 | 000 => 010 
            num = num | head.val
        
        # Return the final decimal value
        return num