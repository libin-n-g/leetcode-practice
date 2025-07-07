# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous pointer as None (will become new head after reversal)
        prev = None
        # Initialize current pointer to head of the list
        curr = head
        
        # Traverse the list until current pointer reaches None (end of list)
        while curr:
            # Store the next node to avoid losing it when reversing the link
            next_node = curr.next
            # Reverse the link: point current node's next to previous node
            curr.next = prev
            # Move previous pointer one step forward to current node
            prev = curr
            # Move current pointer one step forward to next node
            curr = next_node
        
        # Return the new head of the reversed list (prev points to last non-None node)
        return prev