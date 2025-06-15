class Solution:
    def maxDiff(self, num: int) -> int:
        # Convert number to a deque of digits for easier manipulation
        digits = deque()
        while num:
            digits.appendleft(num % 10)  # Extract last digit
            num = num // 10  # Remove last digit
        N = len(digits)  # Store length of number
        
        # Example: num = 555 -> digits = deque([5, 5, 5]), N = 3
        # Example: num = 1234 -> digits = deque([1, 2, 3, 4]), N = 4

        # Get first x and y to maximize the number (a)
        i = 0
        first_x = first_y = 9  # Initialize x and y for first operation
        while i < N and digits[i] == 9: i += 1  # Skip leading 9s to find a non-9 digit
        if i < N:
            first_x = digits[i]  # Set x to first non-9 digit
        # first_y remains 9 to maximize the number
        
        # Example: num = 999 -> first_x = 9, first_y = 9 (no change needed)
        # Example: num = 123 -> first_x = 1, first_y = 9 (replace 1 with 9)

        # Get second x and y to minimize the number (b)
        i = 0
        second_x = second_y = 1  # Initialize x and y for second operation
        while i < N and digits[i] <= 1: i += 1  # Skip digits <= 1 to find a digit > 1
        if i < N: second_x = digits[i]  # Set x to first digit > 1
        # Get second y to minimize the number
        if i != 0 and i < N: second_y = 0  # Use 0 if possible to minimize further
        
        # Example: num = 111 -> second_x = 1, second_y = 1 (no change needed)
        # Example: num = 123 -> second_x = 2, second_y = 0 (replace 2 with 0)

        # Reconstruct the difference (a - b)
        new_num = 0
        for x in digits:
            if x == first_x and x == second_x:
                x = (first_y - second_y)  # Handle case where same digit is used for both
            elif x == first_x:
                x = first_y - x  # Contribution to a (maximized)
            elif x == second_x:
                x = x - second_y  # Contribution to b (minimized)
            else:
                x = 0  # No contribution if digit doesn't match x
            new_num = new_num * 10 + x  # Build the difference digit by digit
        
        # Example: num = 555 -> first_x = 5, first_y = 9, second_x = 5, second_y = 1
        # -> Each digit: 9-1 = 8 -> new_num = 888
        # Example: num = 9 -> first_x = 9, first_y = 9, second_x = 9, second_y = 1
        # -> Digit: 9-1 = 8 -> new_num = 8

        return new_num