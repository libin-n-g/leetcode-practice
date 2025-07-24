class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Define the two substring patterns to remove
        first_condition, second_condition = "ab", "ba"
        
        # If x < y, swap x and y, and swap conditions to prioritize higher points
        if x < y:
            x, y = y, x
            first_condition, second_condition = second_condition, first_condition
        
        # Stack to track characters for first condition removal
        first_condition_stack = []
        # Initialize score to track total points
        score = 0
        
        # First pass: Remove pairs matching first_condition to maximize score
        for c in s:
            # Check if current character and last stack character form first_condition
            if first_condition_stack and \
                first_condition[0] == first_condition_stack[-1] and first_condition[1] == c:
                score += x  # Add points for removing the pair
                first_condition_stack.pop()  # Remove the last character from stack
            else:
                first_condition_stack.append(c)  # Add current character to stack
        
        # Stack for second condition removal
        second_condition_stack = []
        # Second pass: Remove pairs matching second_condition from remaining characters
        for c in first_condition_stack:
            # Check if current character and last stack character form second_condition
            if second_condition_stack and \
                second_condition[0] == second_condition_stack[-1] and second_condition[1] == c:
                score += y  # Add points for removing the pair
                second_condition_stack.pop()  # Remove the last character from stack
            else:
                second_condition_stack.append(c)  # Add current character to stack
        
        # Return total points accumulated
        return score