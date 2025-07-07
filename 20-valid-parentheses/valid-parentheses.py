class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary mapping closing brackets to their corresponding opening brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []  # Stack to store opening brackets
        
        # Iterate through each character in the string
        for c in s:
            # If stack is not empty and current character is a closing bracket that matches the last opening bracket
            if stack and mapping.get(c) == stack[-1]:
                stack.pop()  # Remove the matching opening bracket from the stack
            else:
                stack.append(c)  # Add the character (opening or unmatched closing bracket) to the stack
        
        # String is valid if the stack is empty (all brackets matched)
        if len(stack) == 0:
            return True
        return False  # Non-empty stack means unmatched brackets remain