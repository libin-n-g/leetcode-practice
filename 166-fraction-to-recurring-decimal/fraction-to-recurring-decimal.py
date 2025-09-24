class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle the sign of the result
        negative = False
        if numerator < 0:
            numerator = -numerator
            negative = not negative
        if denominator < 0:
            negative = not negative
            denominator = -denominator
        
        # Calculate the integer part of the division
        result = str(numerator // denominator)
        
        # Get the remainder for fractional part calculation
        numerator = numerator % denominator
        
        # Initialize lists to store fractional digits and numerators
        fractions = []
        numerator_list = [numerator]
        seen_numerator = set(numerator_list)
        
        # Process the fractional part
        while numerator:
            # Multiply numerator by 10 for next decimal place
            numerator = 10 * numerator
            
            # Check for repeating decimal
            if numerator in seen_numerator:
                numerator = numerator // 10
                break
                
            seen_numerator.add(numerator)
            
            # Calculate current decimal digit
            curr_fraction = str((numerator) // denominator)
            numerator = numerator % denominator
            fractions.append(curr_fraction)
            numerator_list.append(numerator)
        
        # Add decimal point if there are fractional digits
        if fractions:
            result += "."
        
        # Construct the fractional part, adding parentheses for repeating decimals
        for num, frac in zip(numerator_list, fractions):
            if num == numerator != 0:
                result += "("
            result += frac
        
        # Close parentheses for repeating decimals
        if "(" in result:
            result += ")"
        
        # Add negative sign if necessary
        if negative and result != "0":
            result = "-" + result
            
        return result